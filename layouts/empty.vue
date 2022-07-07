<template>
  <div>
    <main>
      <Nuxt />
    </main>
  </div>
</template>

<script>
export default {
  name: 'Empty',
  head () {
    return {
      bodyAttrs: {
        class: 'body-margin'
      }
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/main";
</style>
