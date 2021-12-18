<template>
  <div class='footer'>
    <div class='footer-content'>
      <div class='right-side-footer'>
        <nuxt-link to='/' style='text-decoration: none; padding-top: 5px'><p>Home</p></nuxt-link>
        <nuxt-link to='/blog' style='text-decoration: none; padding-top: 5px'><p>Blog</p></nuxt-link>
        <nuxt-link to='/contact' style='text-decoration: none; padding-top: 5px'><p>Contact</p></nuxt-link>
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
