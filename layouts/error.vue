<template>
  <div class="error-page">
    <div class="error">
      <h1>You shouldn't be here! >:(</h1>
      <p>
        <nuxt-link class='nuxt-link' to='/'>
          Go
        </nuxt-link>
        and find some cool staff out of here!
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Error"
}
</script>

<style lang='scss'>
@import '../assets/css/error';
</style>
