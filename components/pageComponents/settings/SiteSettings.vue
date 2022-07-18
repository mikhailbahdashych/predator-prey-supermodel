<template>
  <div class="account-preferences">
    <div class="item">
      <div class="item-content">
        <div class="item-content texts">
          <h3>Change color theme</h3>
          <p class="opacity">Change theme between dark and light.</p>
        </div>
        <div class="item-content">
          <toggle-switch :value="darkTheme" @input="changeTheme" />
        </div>
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
      darkTheme: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  mounted() {
    const theme = localStorage.getItem('_t')
    this.darkTheme = theme === '_d'
  },
  methods: {
    changeTheme() {
      this.darkTheme = !this.darkTheme
      document.documentElement.setAttribute("data-theme", this.darkTheme ? "dark" : "light");
      localStorage.setItem('_t', this.darkTheme ? "_d" : "_l")
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/account/settings";
</style>
