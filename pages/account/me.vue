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
    </div>

  </div>
</template>

<script>
// import Button from "~/components/Button";
// import Skeleton from "~/components/skeleton/Skeleton";
import Input from "~/components/Input";
import { getUserByToken } from "~/api";
export default {
  name: "Index",
  components: {
    // Button,
    // Skeleton
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
