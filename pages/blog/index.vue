<template>
  <div>
    <SideBar :subpages='subpages' />
    <Search />
    <div class='blog-page'>
      <h1 class='big-text centered'>Check out those releases &#128293;</h1>
      <div class='latest-releases'>

        <div class='container-block'>
          <div class='items'>
            <div v-for='post in posts.slice(0, 2)' :key='post.id' class='post-preview main-page-blog' @click='toPost(post.id, post.type)'>
              <div class='post-preview-img' v-html='post.cover'></div>
              <div class='post-preview-content main-page-blog-preview-content'>
                <p>{{ post.title }}</p>
                <p class='plot' v-html='post.plot'></p>
                <p class='date'>Posted at: {{ post.created_at }}</p>
              </div>
            </div>
          </div>
          <div class='items'>
            <div v-for='post in posts.slice(2, 4)' :key='post.id' class='post-preview main-page-blog' @click='toPost(post.id, post.type)'>
              <div class='post-preview-img' v-html='post.cover'></div>
              <div class='post-preview-content main-page-blog-preview-content'>
                <p>{{ post.title }}</p>
                <p class='plot' v-html='post.plot'></p>
                <p class='date'>Posted at: {{ post.created_at }}</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import moment from 'moment'
import Footer from '~/components/Footer';
import SideBar from '~/components/SideBar';
import Search from '~/components/Search';
import { getLatestReleases } from '~/api';
export default {
  name: 'Blog',
  components: {
    Footer,
    SideBar,
    Search
  },
  data() {
    return {
      posts: [],
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
    this.posts = await getLatestReleases(4)
    Object.keys(this.posts).forEach(x => { this.posts[x].created_at = moment(this.posts[x].created_at).format('YYYY-MM-DD HH:mm:ss') })
  },
  methods: {
    toPost(id, type) {
      this.$router.push({
        path: `blog/${type + 's'}/${id}`
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/blog";
@import "../../assets/css/search";
</style>
