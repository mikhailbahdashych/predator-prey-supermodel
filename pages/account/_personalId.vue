<template>
  <div>
    <Popup v-if="showPopup" :content="'Copied!'" />
    <div class="account">
      <div class="side-bar">
        <div class="relative flex">
          <img class="picture" :src="require('../../assets/img/testava.jpg')" alt="ava">
          <p v-if="user.status" class="status nmp">{{ user.status }}</p>
        </div>

        <div class="links pointer" @click="copy('gh')">
          <img :src="require('../../assets/img/github.svg')" alt="Git" class="link">
          <Input v-model="user.github" :additional-class="'small pointer'" :readonly="true" />
          <input id="gh" :value="`${user.github}`" type="hidden">
        </div>

        <div class="links pointer" @click="copy('tw')">
          <img :src="require('../../assets/img/twitter.svg')" alt="Git" class="link">
          <Input v-model="user.twitter" :additional-class="'small pointer'" :readonly="true" />
          <input id="tw" :value="`${user.twitter}`" type="hidden">
        </div>

        <div class="links pointer" @click="copy('wl')">
          <img :src="require('../../assets/img/tag.svg')" alt="Git" class="link">
          <Input v-model="user.website_link" :additional-class="'small pointer'" :readonly="true" />
          <input id="wl" :value="`${user.website_link}`" type="hidden">
        </div>

        <Button
          v-if="isOwner"
          :label="'Edit profile'"
          :additional-class="'transparent min-width150 mt'"
          @click-handler="redirect('/account/settings')"
        />
        <Button
          v-else
          :label="'Send message'"
          :additional-class="'transparent min-width150 mt'"
          @click-handler="redirect('/account/settings')"
        />
      </div>

      <div class="content">
        <div class="title">
          <div class="flex baseline">
            <h1 class="nmp">{{ user.username }}</h1>
            <p v-if="user.first_name || user.last_name" class="paragraph">
              aka {{ user.first_name }} {{ user.last_name }}
            </p>
            <p class="paragraph">({{ user.personalId }})</p>
          </div>
          <p class="paragraph opacity">{{ user.about_me }}</p>
          <div>
          </div>
        </div>
        <div class="flex">
          <div class="item border">
            <h2 class='font-second center'>Latest forum posts</h2>
          </div>
          <div class="item border">
            <h2 class='font-second center'>Latest Q&A posts</h2>
          </div>
          <div class="item">
            <h2 class='font-second center'>Latest blog posts</h2>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Button from "~/components/Button";
import Popup from "~/components/Popup";
import Input from "~/components/Input";
import { getUserByPersonalId } from "~/api";
import { verifyToken } from "~/helpers/crypto";
export default {
  name: 'PersonalId',
  components: {
    Button,
    Popup,
    Input
  },
  data() {
    return {
      user: {},
      loading: true,
      showPopup: false,
      isOwner: false
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    return await this.getCurrentUser()
  },
  methods: {
    async getCurrentUser() {
      this.user = await getUserByPersonalId(this.$route.params.personalId)

      if (this.user.personalId === verifyToken(sessionStorage.getItem('_at')).personalId)
        this.isOwner = true
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
@import "../../assets/css/account";
</style>
