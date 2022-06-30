<template>
  <div class='account'>
    <div class='account-content'>
      <img class='account-header-avatar' src="../../assets/img/testava.jpg" alt="ava">
      <div class='account-header-data'>
        <h1 class='font-second'>{{user.username}}</h1>
        <div v-if="isOwner" class="account-header-data">
          <Button :label="'Edit profile'" :additional-class="'transparent'" class="buttons" />
          <Button :label="'Settings'" :additional-class="'transparent'" class="buttons" @click-handler="redirect('/account/settings')" />
        </div>
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
import {getUserByToken, getUserByPersonalId} from '~/api';
import {validateUserPersonalId} from '~/helpers/frontValidator';
import Button from '~/components/Button'
export default {
  name: 'PersonalId',
  components: {
    Button
  },
  data() {
    return {
      user: {},
      isOwner: false
    }
  },
  async mounted() {
    if (!this.$route.params.personalId)
      return await this.$router.push('/')
    else if (!validateUserPersonalId(this.$route.params.personalId))
      return await this.$router.push('/')
    else if (localStorage.getItem('token'))
      return await this.getCurrentUser(localStorage.getItem('token'))
    await this.getUser(this.$route.params.personalId)
  },
  methods: {
    async getUser(personalId) {
      this.user = await getUserByPersonalId(personalId)
    },
    async getCurrentUser(token) {
      this.user = await getUserByToken(token)

      if (!this.user)
        return await this.$router.push('/')

      if (this.user.personalId === this.$route.params.personalId)
        this.isOwner = true
    },
    redirect(path) {
      this.$router.push({ path })
    },
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/account";
</style>
