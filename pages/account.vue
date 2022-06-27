<template>
  <div class='account'>
    <div class='account-header'>
      <div class='account-header-avatar' />
      <div class='account-header-data'>
        <h1>@username</h1>
      </div>
      <div class='account-header-buttons'>
        <span class='account-header-button'><Button :label="'Edit profile'" :additional-class="'transparent'" /></span>
        <span class='account-header-button'><Button :label="'Settings'" :additional-class="'transparent'" /></span>
      </div>
    </div>
  </div>
</template>

<script>
import Button from '~/components/Button'
export default {
  name: "Account",
  components: {
    Button
  },
  data() {
    return {

    }
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../assets/css/account";
</style>
