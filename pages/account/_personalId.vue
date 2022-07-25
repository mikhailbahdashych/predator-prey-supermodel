<template>
  <div>
    <Popup v-if="showPopup" :content="'Copied!'" />
    <div class="account">
      <div class="account__side-bar">
        <div class="account__ava">
          <img class="account__picture" :src="require('../../assets/img/testava.jpg')" alt="ava">
          <p v-if="user.user_status" class="account__status">{{ user.user_status }}</p>
        </div>

        <skeleton v-if="loading" />
        <skeleton v-if="loading" />
        <skeleton v-if="loading" />

        <div v-if="user.github || user.twitter || user.website_link" class="account__social-title">
          <h4>Social media</h4>
          <hr>
        </div>

        <div v-if="user.github && !loading" class="account__links" @click="copy('gh')">
          <img :src="require('../../assets/img/github.svg')" alt="Git" class="account__link">
          <Input v-model="user.github" :input-class="'bi--basic-input__small bi--basic-input__pointer'" :readonly="true" />
          <input id="gh" :value="`${user.github}`" type="hidden">
        </div>

        <div v-if="user.twitter && !loading" class="account__links" @click="copy('tw')">
          <img :src="require('../../assets/img/twitter.svg')" alt="Git" class="account__link">
          <Input v-model="user.twitter" :input-class="'bi--basic-input__small bi--basic-input__pointer'" :readonly="true" />
          <input id="tw" :value="`${user.twitter}`" type="hidden">
        </div>

        <div v-if="user.website_link && !loading" class="account__links" @click="copy('wl')">
          <img :src="require('../../assets/img/tag.svg')" alt="Git" class="account__link">
          <Input v-model="user.website_link" :input-class="'bi--basic-input__small bi--basic-input__pointer'" :readonly="true" />
          <input id="wl" :value="`${user.website_link}`" type="hidden">
        </div>

        <div v-if="user.company || user.location" class="account__social-title">
          <h4 v-if="user.location && !user.company">Location</h4>
          <h4 v-else-if="user.company && !user.location">Place of work</h4>
          <h4 v-else>Location and place of work</h4>
          <hr>
        </div>

        <div v-if="user.company || user.location">
          <div v-if="user.location && !user.company" class="account__links">
            <img :src="require('../../assets/img/location.svg')" alt="Loc" class="account__link">
            {{ user.location }}
          </div>
          <div v-else-if="user.company && !user.location" class="account__links">
            <img :src="require('../../assets/img/company.png')" alt="Company" class="account__link">
            <p>{{ user.company }}</p>
          </div>
          <div v-else>
            <div class="account__links">
              <img :src="require('../../assets/img/location.svg')" alt="Loc" class="account__link">
              <Input v-model="user.location" :input-class="'bi--basic-input__small'" :readonly="true" />
            </div>
            <div class="account__links">
              <img :src="require('../../assets/img/company.png')" alt="Company" class="account__link">
              <Input v-model="user.company" :input-class="'bi--basic-input__small'" :readonly="true" />
            </div>
          </div>
        </div>

        <div v-if="user.show_email" class="account__social-title">
          <h4>Contact email</h4>
        </div>

        <div class="account__side-bar_buttons">
          <div v-if="isOwner && !loading" class="account__item">
            <Button
              :label="'Edit profile'"
              :btn-class="'basic-button--transparent'"
              @click-handler="redirect('/account/settings')"
            />
          </div>
          <div v-if="isOwner && !loading" class="account__item">
            <Button
              :label="'My bookmarks'"
              :btn-class="'basic-button--transparent'"
              @click-handler="redirect('/account/bookmarks')"
            />
          </div>
          <div v-else-if="!isOwner && !loading" class="account__item">
            <Button
              :label="'Send message'"
              :btn-class="'basic-button--transparent'"
              @click-handler="redirect('/account/settings')"
            />
          </div>
        </div>
      </div>

      <div class="account__last-activity">
        <div class="account__title">
          <skeleton v-if="loading" />
          <div v-else class="account__info">
            <div class="account__info">
              <h1>{{ user.username }}</h1>
              <p v-if="user.first_name || user.last_name">
                aka {{ user.first_name }} {{ user.last_name }}
              </p>
              <p class="account__id" >({{ user.personalId }})</p>
            </div>
            <div>
              <h3><span class="source-sans-pro bold">Reputation: </span>{{ user.reputation }}</h3>
            </div>
          </div>
          <div v-if="loading">
            <div v-for="(s, i) of 3" :key="i">
              <skeleton :width="250" />
            </div>
          </div>
          <p v-else class="account__about-title">{{ user.about_me }}</p>
        </div>

        <div class="account__header">
          <div v-for="item in subpageItems" :key="item.title" :class="[item.active ? 'active' : '']" class="account__box">
            <p :class="[item.active ? 'active' : '']" class="account__item" @click="changeSubpage(item)">
              {{item.title}}
            </p>
          </div>
        </div>

        <div v-if="currentSubpage === 'Forum posts'" class="account__subpage-item">
          <div v-if="!userLastActivity.forumPosts.length" class="account__no-posts">
            <h2>Latest forum posts</h2>
            <p class="opacity">No forum posts yet.</p>
          </div>
          <div v-else>
            <p>{{ userLastActivity.forumPosts }}</p>
          </div>
        </div>
        <div v-else-if="currentSubpage === 'Questions and answers'" class="account__subpage-item">
          <div v-if="!userLastActivity.usersQuestions.length" class="account__no-posts">
            <h2>Latest Q&A posts</h2>
            <p class="opacity">No Q&A posts yet.</p>
          </div>
          <div v-if="userLastActivity.usersQuestions.length" class="account__sort-bar">
            <p
              v-for="item in sortTypes"
              :key="item.title"
              class="account__sort-bar-item"
              :class="item.active ? 'account__sort-bar-item--active' : ''"
            >
              <span
                :class="!item.active ? 'opacity' : ''"
                @click="sortBy(item)"
              >{{ item.title }}</span>
            </p>
          </div>
          <div v-if="userLastActivity.usersQuestions.length">
            <div
              v-for="q in userLastActivity.usersQuestions"
              :key="q.slug"
              @click="redirect(`/qa/question/${q.slug}`)"
            >
              <div class="account__qa">
                <div class="account__qa-title">
                  <h3>{{ q.title }}</h3>
                  <p class="opacity">Asked at: {{ q.created_at }}</p>
                </div>
                <div class="account__qa-items">
                  <p class="account__preview-block">Views: {{ q.views }}</p>
                  <p class="account__preview-block">Answers: {{ q.count || 0 }}</p>
                  <p
                    class="account__preview-block account__preview-block--answer"
                    :class="q.is_answered ? 'account__preview-block--answered' : q.votes < 0 ? 'account__preview-block--low-quality-question' : ''">
                    Votes: {{ q.votes }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="account__subpage-item">
          <div v-if="!userLastActivity.usersBlogPosts.length" class="account__no-posts">
            <h2>Latest blog posts</h2>
            <p class="opacity">No blog posts yet.</p>
          </div>
          <div v-else>
            <p>{{ userLastActivity.usersBlogPosts }}</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Skeleton from '~/components/skeleton/Skeleton'
import Button from '~/components/basicComponents/Button'
import Popup from '~/components/basicComponents/Popup'
import Input from '~/components/basicComponents/Input'
import { getUserByPersonalId, getUserQuestions } from '~/api'
import { verifyToken } from '~/helpers/crypto'
import { validateUserPersonalId } from '~/helpers/frontValidator'
export default {
  name: 'PersonalId',
  components: {
    Skeleton,
    Button,
    Popup,
    Input
  },
  validate({ params }) { return validateUserPersonalId(parseInt(params.personalId)) },
  data() {
    return {
      user: {},
      userLastActivity: {
        forumPosts: [],
        usersQuestions: [],
        usersBlogPosts: []
      },
      loading: true,
      showPopup: false,
      isOwner: false,

      subpageItems: [
        { title: 'Forum posts', active: true },
        { title: 'Questions and answers', active: false },
        { title: 'Blog posts', active: false }
      ],
      currentSubpage: 'Forum posts',

      sortTypes: [
        { title: 'Latest', active: true },
        { title: 'Score', active: false },
        { title: 'Views', active: false }
      ],
      currentSortType: 'Latest'
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.getCurrentUser()
    await this.getUserQuestions()
  },
  methods: {
    async getUserQuestions() {
      this.userLastActivity.usersQuestions = await getUserQuestions({
        personalId: this.$route.params.personalId,
        sort: this.currentSortType.toLowerCase()
      })
    },
    async getCurrentUser() {
      this.user = await getUserByPersonalId(this.$route.params.personalId)
      this.isOwner = this.user.personalId === verifyToken(sessionStorage.getItem('_at')).personalId
    },
    sortBy(item) {
      this.sortTypes.forEach(type => { type.active = type.title === item.title })
      this.currentSortType = item.title
      this.getUserQuestions()
    },
    changeSubpage(subpage) {
      this.subpageItems.forEach(sub => { sub.active = sub.title === subpage.title })
      this.currentSubpage = subpage.title
    },
    redirect(path) {
      return this.$router.push(path)
    },
    copy(t) {
      const input = document.querySelector(`#${t}`)
      input.setAttribute('type', 'text')
      input.select()
      document.execCommand('copy')
      input.setAttribute('type', 'hidden')

      this.showPopup = true

      setTimeout(() => { this.showPopup = false }, 1500)
    },
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/pages/account";
</style>
