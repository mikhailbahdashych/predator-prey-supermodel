<template>
  <div class="error-page">
    <h1 class="error-page__text error-page__text--head">Page not found</h1>
    <p class="error-page__text error-page__text--paragraph">Sorry, but we are unable to find whatever you are looking for.</p>
    <p class="error-page__text error-page__text--paragraph">
      <nuxt-link class='error-page__text--nuxt-link' to='/'>
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
