<template>
  <div>
    <Header />
    <div class='contact'>
      <h1>contact page</h1>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from '~/components/Header';
import Footer from '~/components/Footer'
export default {
  name: 'Contact',
  components: {
    Header,
    Footer
  },
  data() {
    return {

    }
  }
}
</script>

<style lang='scss'>
@import "assets/css/contact";
</style>
