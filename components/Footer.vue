<template>
  <div class='footer'>
    <div class='footer-content'>
      <div class='right-side-footer'>
        <nuxt-link to='/' class='nuxt-link'><p>Home</p></nuxt-link>
        <nuxt-link to='/blog' class='nuxt-link'><p>Blog</p></nuxt-link>
        <nuxt-link to='/contact' class='nuxt-link'><p>Contact</p></nuxt-link>
      </div>
      <div class='left-side-footer'>
        <p>© All rights reserved 2021, Mikhail Bahdashych, pNb</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style lang='scss'>
@import "assets/css/footer";
</style>
