<template>
  <div>
    <SideBar />
    <div class='blog-header'>
      <div class='search-div'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='post-content'>
      <h1 class='big-text post-title'>{{ post.title }}</h1>
      <p v-html='post.text'></p>
    </div>
    <Footer />
  </div>
</template>

<script>
import { getArticleById, getWriteUpById, getCtfById } from '~/api';
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
      post: {}
    }
  },
  async mounted() {
    await this.getPostByTypeAndId()
  },
  methods: {
    async getPostByTypeAndId() {
      if (this.$route.params.category === 'article') {
        this.post = await getArticleById(this.$route.params.id)
      } else if (this.$route.params.category === 'ctf') {
        this.post = await getCtfById(this.$route.params.id)
      } else {
        this.post = await getWriteUpById(this.$route.params.id)
      }
    }
  }
}
</script>

<style lang='scss'>
@import "../../../assets/css/post";
</style>
