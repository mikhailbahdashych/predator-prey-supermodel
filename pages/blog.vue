<template>
  <div>
    <SideBar />
    <div class='blog-header'>
      <div style='padding-top: 20px'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='blog-page'>
      <h1>Check out those releases</h1>
      <div class='latest-releases'>
        <div class="container">

          <div
            v-for="i in 4"
            :key="i"
            :class="listItemStyle(i-1)">
            <div class='content-container'></div>
          </div>

        </div>
      </div>
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
  },
  data() {
    return {
      grids: ['first', 'second', 'third', 'forth']
    }
  },
  methods: {
    listItemStyle(i) {
      return this.grids[i]
    }
  }
}
</script>

<style lang='scss'>
@import "assets/css/blog";
@import "../assets/css/blogheader";
</style>
