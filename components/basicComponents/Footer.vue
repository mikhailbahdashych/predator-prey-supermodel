<template>
  <footer class='footer'>
    <div class='footer-content'>
      <div class='right-side-footer'>
        <nuxt-link to='/' class='nuxt-link'><p class='texts'>Home</p></nuxt-link>
        <nuxt-link to='/forum' class='nuxt-link'><p class='texts'>Forum</p></nuxt-link>
        <nuxt-link to='/qanda' class='nuxt-link'><p class='texts'>Q&A</p></nuxt-link>
        <nuxt-link to='/blog' class='nuxt-link'><p class='texts'>Blog</p></nuxt-link>
      </div>
      <div class='left-side-footer'>
        <p class='texts'>© All rights reserved, 2021</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
}
</script>

<style lang='scss'>
@import "../../assets/css/basicComponents/Footer";
</style>
