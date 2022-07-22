<template>
  <div class="error-page center">
    <h1 class="text head">Page not found</h1>
    <p class="text">Sorry, but we are unable to find whatever you are looking for.</p>
    <p class="text">
      <nuxt-link class='nuxt-link' to='/'>
        Go back
      </nuxt-link>
      and try one more time.
    </p>
  </div>
</template>

<script>
export default {
  name: "Error",
  layout: 'header-only',
  head () {
    return {
      bodyAttrs: {
        class: 'body-margin'
      }
    }
  }
}
</script>

<style lang='scss'>
@import '../assets/css/pages/error';
@import '../assets/css/main';
</style>
