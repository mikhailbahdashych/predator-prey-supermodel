<template>
  <div class="header">
    <div class="inner-header">
      <nuxt-link to="/" style="text-decoration: none; color: white"><h3>HOME</h3></nuxt-link>
      <nuxt-link to="/blog" style="text-decoration: none; color: white"><h3>BLOG</h3></nuxt-link>
      <nuxt-link to="/contact" style="text-decoration: none; color: white"><h3>CONTACT</h3></nuxt-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style lang='scss'>
@import '../assets/css/main';
</style>
