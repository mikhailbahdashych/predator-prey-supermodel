<template>
  <div class='account'>
    <div class='account-header'>
      <div class='account-header-avatar' />
      <div class='account-header-data'>
        <h1>{{user.nickname}}</h1>
      </div>
      <div v-if='isOwner' class='account-header-buttons'>
        <span class='account-header-button'>
          <Button :label="'Edit profile'" :additional-class="'transparent'" />
        </span>
        <span class='account-header-button'>
          <Button :label="'Settings'" :additional-class="'transparent'" />
        </span>
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
    }
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/account";
</style>
