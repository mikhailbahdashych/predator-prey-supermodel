<template>
  <div class="account">
    <div class="side-bar">
      <img class="picture" :src="require('../../assets/img/testava.jpg')" alt="ava">

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

      <Button :label="'Send message'" :additional-class="'mt min-width150'" />
    </div>

    <div class="content">
      <div class="title">
        <div class="flex">
          <h1 class="nmp">{{ user.username }}</h1>
          <div>
            <Button
              @click-handler="redirect('/account/settings')"
              :label="'Edit profile'"
              :additional-class="'transparent min-width150 mrl'"
            />
          </div>
        </div>
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
import { getUserByToken } from "~/api";
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
    if (sessionStorage.getItem('token'))
      return await this.getCurrentUser(sessionStorage.getItem('token'))
    else
      return this.$router.push('/')
  },
  methods: {
    async getCurrentUser(token) {
      this.user = await getUserByToken(token)

      if (this.user.status === -1) {
        sessionStorage.removeItem('token')
        sessionStorage.removeItem('personalId')
        return this.$router.push('/')
      }
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
