<template>
  <div class="header">
    <div class="inner-header">
      <nuxt-link to="/" class='nuxt-link'><h3>HOME</h3></nuxt-link>
      <nuxt-link id='blog-button-link' to="/blog" class='nuxt-link'><h3>BLOG</h3></nuxt-link>
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
