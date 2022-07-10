<template>
  <div class="account">
    <div class="side-bar">
      <img class="picture" :src="require('../../assets/img/testava.jpg')" alt="ava">

    </div>

  </div>
</template>

<script>
// import Button from "~/components/Button";
// import Skeleton from "~/components/skeleton/Skeleton";
import { getUserByToken } from "~/api";
export default {
  name: "Index",
  components: {
    // Button,
    // Skeleton
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
