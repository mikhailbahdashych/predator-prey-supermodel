<template>
  <div>
    <SideBar :subpages='subpages' />
    <div class='blog-header'>
      <div class='search-div'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='blog-page'>
      <h1 class='big-text'>Check out those releases &#128293;</h1>
      <div class='latest-releases'>
        <div class="container">

          <div
            v-for="i in 4"
            :key="i"
            :class="listItemStyle(i-1)"
            @click='toPost(i)'
          >
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
      grids: ['first', 'second', 'third', 'forth'],
      subpages: [
        {name: 'Blog main page', value: 'bmp', page: '/blog', status: true},
        {name: 'Articles', value: 'article', page: '/blog/articles', status: false},
        {name: 'Write-ups', value: 'writeup', page: '/blog/writeups', status: false},
        {name: 'Tips', value: 'tip', page: '/blog/tips', status: false},
        {name: 'CTF\'s', value: 'ctf', page: '/blog/ctfs', status: false},
      ]
    }
  },
  async mounted() {

  },
  methods: {
    listItemStyle(i) {
      return this.grids[i]
    },
    toPost(id) {
      this.$router.push({
        path: `blog/post/${id}`
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/blog";
@import "../../assets/css/blogheader";
</style>
