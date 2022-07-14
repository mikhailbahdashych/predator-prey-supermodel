<template>
  <div class="account">
    <div class="side-bar">
      <div class="relative flex">
        <img class="picture" :src="require('../../assets/img/testava.jpg')" alt="ava">
        <p v-if="user.title" class="status nmp">{{ user.title }}</p>
      </div>

      <div class="links">
        <img :src="require('../../assets/img/github.svg')" alt="Git" class="link">
        <Input
          v-model="user.github"
          :additional-class="'small'"
          :readonly="true"
        />
      </div>

      <div class="links">
        <img :src="require('../../assets/img/twitter.svg')" alt="Git" class="link">
        <Input
          v-model="user.twitter"
          :additional-class="'small'"
          :readonly="true"
        />
      </div>

      <div class="links">
        <img :src="require('../../assets/img/tag.svg')" alt="Git" class="link">
        <Input
          v-model="user.website_link"
          :additional-class="'small'"
          :readonly="true"
        />
      </div>

      <Button
        :label="'Edit profile'"
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
</template>

<script>
import Button from "~/components/Button";
import Input from "~/components/Input";
import { getUserByAccessToken, getRefreshedTokens } from "~/api";
export default {
  name: "Index",
  components: {
    Button,
    Input
  },
  data() {
    return {
      user: {},
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    if (sessionStorage.getItem('accessToken'))
      return await this.getCurrentUser(sessionStorage.getItem('accessToken'))
    else
      return this.$router.push('/')
  },
  methods: {
    async getCurrentUser(token) {
      this.user = await getUserByAccessToken(token)

      if (this.user.status === -1) {
        sessionStorage.removeItem('accessToken')
        return this.$router.push('/')
      }

      const { accessToken } = await getRefreshedTokens(sessionStorage.getItem('accessToken'))
      sessionStorage.setItem('accessToken', accessToken)
    },
    redirect(path) {
      return this.$router.push(path)
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/account";
</style>
