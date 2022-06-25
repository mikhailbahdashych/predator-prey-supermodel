<template>
  <div class="header">
    <div class="inner-header">
      <div class="header-content">
        <div class="header-content">
          <nuxt-link to="/" class='nuxt-link'><h3>pNb</h3></nuxt-link>
          <nuxt-link to="/" class='nuxt-link'><h3>FORUM</h3></nuxt-link>
          <nuxt-link to="/" class='nuxt-link'><h3>Q&A</h3></nuxt-link>
          <nuxt-link to="/" class='nuxt-link'><h3>BLOG</h3></nuxt-link>
        </div>
        <div class="header-content">
          <nuxt-link to="/" class='nuxt-link'><h3>SIGN IN</h3></nuxt-link>
          <nuxt-link to="/" class='nuxt-link'><h3>SIGN UP</h3></nuxt-link>
        </div>
      </div>
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
