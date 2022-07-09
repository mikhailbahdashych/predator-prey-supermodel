<template>
  <div class='account'>
    <div class='account-content'>
      <img class='account-header-avatar' src="../../assets/img/testava.jpg" alt="ava">
      <div class='account-header-data'>
        <skeleton v-if="loading" :text="'username'" />
        <h1 v-else class='font-second'>{{user.username}}</h1>
        <h3 class="font-second"></h3>
        <Button :label="'Settings'" :additional-class="'transparent'" class="buttons" @click-handler="redirect('/account/settings')" />
      </div>
    </div>

    <div class="account-content activity">
      <div class="section-activity border">
        <h2 class='font-second center'>Last forum activity</h2>
      </div>
      <div class="section-activity border">
        <h2 class='font-second center'>Last Q&A activity</h2>
      </div>
      <div class="section-activity">
        <h2 class='font-second center'>Last blog activity</h2>
      </div>
    </div>

  </div>
</template>

<script>
import Button from "~/components/Button";
import Skeleton from "~/components/skeleton/Skeleton";
import { getUserByToken } from "~/api";
export default {
  name: "Index",
  components: {
    Button,
    Skeleton
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
    if (localStorage.getItem('token'))
      return await this.getCurrentUser(localStorage.getItem('token'))
    else
      return await this.$router.push('/')
  },
  methods: {
    async getCurrentUser(token) {
      this.user = await getUserByToken(token)

      if (this.user.status === -1) {
        localStorage.removeItem('token')
        localStorage.removeItem('personalId')
        return await this.$router.push('/')
      }
    },
    redirect(path) {
      this.$router.push(path)
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/account";
</style>
