<template>
  <div class="page-content">
    <div class="content-wrap">
      <Header />
      <main>
        <Nuxt/>
      </main>
    </div>
  </div>
</template>

<script>
import Header from '~/components/basicComponents/Header';
export default {
  name: 'HeaderOnly',
  components: {
    Header
  },
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
