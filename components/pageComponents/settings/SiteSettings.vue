<template>
  <div class="account-preferences">
    <div class="item-content">
      <div class="item-content texts">
        <h3>Change light theme</h3>
        <p class="opacity">Change theme between dark and light.</p>
      </div>
      <div class="item-content">
        <toggle-switch :value="lightTheme" @input="changeTheme" />
      </div>
    </div>
  </div>
</template>

<script>
import ToggleSwitch from '~/components/basicComponents/ToggleSwitch'
export default {
  name: 'SiteSettings',
  components: {
    ToggleSwitch
  },
  data() {
    return {
      loading: true,
      lightTheme: false
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  methods: {
    changeTheme() {
      this.lightTheme = !this.lightTheme
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/account/settings";
</style>
