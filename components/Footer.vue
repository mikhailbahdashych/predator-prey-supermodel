<template>
  <div class='footer'>
    <div class='footer-content'>
      <div class='right-side'>
        <nuxt-link to='/' style='text-decoration: none; padding-top: 5px'><p>Home</p></nuxt-link>
        <nuxt-link to='' style='text-decoration: none; padding-top: 5px'><p>Blog</p></nuxt-link>
        <nuxt-link to='/contact' style='text-decoration: none; padding-top: 5px'><p>Contact</p></nuxt-link>
      </div>
      <div class='left-side'>
        <p>left side</p>
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
