<template>
  <div>
    <SideBar :subpages='subpages' />
    <div class='blog-header'>
      <div class='search-div'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='post-content'>
      <h1 class='big-text post-title'>{{$route.params}}</h1>
      <h1 class='big-text post-title'>{{ post }}</h1>
      <h1 class='big-text post-title'>{{ posts }}</h1>
    </div>
    <Footer />
  </div>
</template>

<script>
import { getPostById, getPostsByCategory } from '~/api';
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
      post: {},
      posts: [],
      typeOfPosts: null,
      categories: ['articles', 'writeups', 'tips', 'ctfs'],
      subpages: [
        {name: 'Blog main page', value: 'bmp', page: '/blog', status: false},
        {name: 'Articles', value: 'article', page: '/blog/articles', status: false},
        {name: 'Write-ups', value: 'writeup', page: '/blog/writeups', status: false},
        {name: 'Tips', value: 'tip', page: '/blog/tips', status: false},
        {name: 'CTF\'s', value: 'ctf', page: '/blog/ctfs', status: false},
      ]
    }
  },
  async mounted() {
    this.getAndCheckCategory()
    window.scrollBy(0, 70)
    if (this.$route.params.id) await this.getPostById()
    else await this.getPostsByCategory()
  },
  methods: {
    async getPostById() {
      this.post = await getPostById(this.$route.params.id)
    },
    async getPostsByCategory() {
      this.posts = await getPostsByCategory(this.typeOfPosts)
    },
    getAndCheckCategory() {
      if (!this.categories.includes(this.$route.params.category))
        this.$router.push({path: '/blog'})
      this.subpages.forEach(item => {
        if (item.page.includes(this.$route.params.category)) {
          item.status = true
          this.typeOfPosts = item.value
        }
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../../../assets/css/post";
</style>
