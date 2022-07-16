<template>
  <div class="error-page center">
    <h1 class='text head'>You shouldn't be here! >:(</h1>
    <p class='text paragraph'>
      <nuxt-link class='nuxt-link' to='/'>
        Go
      </nuxt-link>
      and find some cool staff out of here!
    </p>
  </div>
</template>

<script>
export default {
  name: "Error",
  layout: 'empty',
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
