<template>
  <div class='main'>
    <Header />
    <div class="content">
      <div class="center-text">
      </div>
    </div>

    <div class="about">
    </div>

    <div class="about blog">
    </div>

    <Footer/>
  </div>
</template>

<script>
import Header from '~/components/Header';
import Footer from '~/components/Footer';
export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      loading: true,
      latestReleases: [],
    }
  },
  head() {
    return {
    }
  },
  methods: {
    toPost(id, type) {
      this.$router.push({
        path: `blog/${type + 's'}/${id}`
      })
    },
  },
}
</script>

<style lang='scss'>
@import "../assets/css/homepage";
</style>
