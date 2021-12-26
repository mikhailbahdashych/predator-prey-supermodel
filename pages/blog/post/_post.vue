<template>
  <div>
    <SideBar />
    <div class='blog-header'>
      <div style='padding-top: 20px'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='blog-page'>
      <h1 v-if='wrongPost'>There is no such post :(</h1>
      <h1 v-else>{{ $route.params }}</h1>
    </div>
    <Footer />
  </div>
</template>

<script>
import Footer from '~/components/Footer';
import SideBar from '~/components/SideBar';
export default {
  name: 'Index',
  components: {
    Footer,
    SideBar,
  },
  data() {
    return {
      wrongPost: false
    }
  },
  created() {
    if (!this.$route.params.post) {
      this.wrongPost = true
    }
  }
}
</script>

<style lang='scss'>
@import "../../../assets/css/post";
</style>
