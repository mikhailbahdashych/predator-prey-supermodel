<template>
  <div>
    <SideBar :subpages='subpages' />
    <Search />
    <div class='blog-page'>
      <h1 class='big-text'>Check out those releases &#128293;</h1>
      <div class='latest-releases'>

        <div class='container-block'>
          <div class='items'>
            <div class='block'><div class='image'></div></div>
            <div class='block'><div class='image'></div></div>
          </div>
          <div class='items'>
            <div class='block'><div class='image'></div></div>
            <div class='block'><div class='image'></div></div>
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
import Search from '~/components/Search'
export default {
  name: 'Blog',
  components: {
    Footer,
    SideBar,
    Search
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
@import "../../assets/css/search";
</style>
