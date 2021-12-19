<template>
  <div>
    <div class='blog-header'>
    </div>
    <SideBar />
    <div class='blog-page'>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from '~/components/Footer';
import SideBar from '~/components/SideBar';
export default {
  name: 'Blog',
  components: {
    Footer,
    SideBar,
  }
}
</script>

<style lang='scss'>
@import "assets/css/blog";
@import "assets/css/blogHeader";
</style>
