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
          <div class="first">
            <div style='height: 100%; width: 20%; background-color: #202021; border-radius: 12px 0 0 12px'></div>
          </div>
          <div class="second">
            <div style='height: 100%; width: 20%; background-color: #202021; border-radius: 12px 0 0 12px'></div>
          </div>
          <div class="third">
            <div style='height: 100%; width: 20%; background-color: #202021; border-radius: 12px 0 0 12px'></div>
          </div>
          <div class="forth">
            <div style='height: 100%; width: 20%; background-color: #202021; border-radius: 12px 0 0 12px'></div>
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
  }
}
</script>

<style lang='scss'>
@import "assets/css/blog";
@import "../assets/css/blogheader";
</style>
