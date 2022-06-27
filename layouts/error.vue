<template>
  <div class="error-page center">
    <h1>You shouldn't be here! >:(</h1>
    <p>
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
  layout: 'empty'
}
</script>

<style lang='scss'>
@import '../assets/css/error';
</style>
