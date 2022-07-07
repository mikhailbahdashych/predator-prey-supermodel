<template>
  <div class="page-content">
    <div class="content-wrap">
      <Header />
      <main>
        <Nuxt/>
      </main>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '~/components/Header';
import Footer from '~/components/Footer';
export default {
  name: 'Default',
  components: {
    Header, Footer
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
