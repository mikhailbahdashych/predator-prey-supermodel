<template>
  <footer class='footer'>
    <div class='footer__footer-content'>
      <div class='footer__footer-content__right-side-footer'>
        <nuxt-link to='/' class='nuxt-link'><p class='footer__footer-content__texts'>Home</p></nuxt-link>
        <nuxt-link to='/forum' class='nuxt-link'><p class='footer__footer-content__texts'>Forum</p></nuxt-link>
        <nuxt-link to='/qa' class='nuxt-link'><p class='footer__footer-content__texts'>Q&A</p></nuxt-link>
        <nuxt-link to='/blog' class='nuxt-link'><p class='footer__footer-content__texts'>Blog</p></nuxt-link>
      </div>
      <div class='footer__footer-content__left-side-footer'>
        <p class='footer__footer-content__texts'>© All rights reserved, 2021</p>
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
