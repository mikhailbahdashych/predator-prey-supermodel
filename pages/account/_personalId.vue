<template>
  <div class='account'>
    <div class='account-content'>
      <img class='account-header-avatar' :src="require('../../assets/img/testava.jpg')" alt="ava">
      <div class='account-header-data'>
        <h1 class='font-second'>{{user.username}}</h1>
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
import { getUserByPersonalId } from '~/api';
import { validateUserPersonalId } from '~/helpers/frontValidator';
export default {
  name: 'PersonalId',
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
    if (!this.$route.params.personalId)
      return this.$router.push('/')
    else if (!validateUserPersonalId(this.$route.params.personalId))
      return this.$router.push('/')
    else if (this.$route.params.personalId === sessionStorage.getItem('personalId'))
      return this.$router.push('/account/me')
    await this.getUser(this.$route.params.personalId)
  },
  methods: {
    async getUser(personalId) {
      this.user = await getUserByPersonalId(personalId)
    },
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/account";
</style>
