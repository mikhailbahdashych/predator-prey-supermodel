<template>
  <footer class='footer'>
    <div class='footer-content'>
      <div class='right-side-footer'>
        <nuxt-link to='/' class='nuxt-link'><p>Home</p></nuxt-link>
        <nuxt-link to='/forum' class='nuxt-link'><p>Forum</p></nuxt-link>
        <nuxt-link to='/qanda' class='nuxt-link'><p>Q&A</p></nuxt-link>
        <nuxt-link to='/blog' class='nuxt-link'><p>Blog</p></nuxt-link>
      </div>
      <div class='left-side-footer'>
        <p>© All rights reserved, 2021</p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style lang='scss'>
@import "../assets/css/components/Footer";
</style>
