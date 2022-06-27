<template>
  <div class='account'>
    <div class='account-header'>
      <div class='account-header-avatar' />
      <div class='account-header-data'>
        <h1>@username</h1>
      </div>
      <div class='account-header-buttons'>
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
import {getUserByToken} from '~/api';
import Button from '~/components/Button'
export default {
  name: "Account",
  components: {
    Button
  },
  data() {
    return {
      user: null
    }
  },
  async mounted() {
    await this.getCurrentUser(localStorage.getItem('token'))
  },
  methods: {
    async getCurrentUser(token) {
      if (token) {
        this.user = await getUserByToken(token)
      }
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/account";
</style>
