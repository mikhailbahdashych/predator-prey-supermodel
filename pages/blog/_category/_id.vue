<template>
  <div>
    <SideBar />
    <div class='blog-header'>
      <div style='padding-top: 20px'>
        <input class='search-field' placeholder='Search...'>
      </div>
    </div>
    <div class='blog-page'>
      <h1>{{ post.title }}</h1>
      <p v-html='post.text'></p>
    </div>
    <Footer />
  </div>
</template>

<script>
import { getArticleById } from '~/api';
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
      }
    }
  }
}
</script>

<style lang='scss'>
@import "../../../assets/css/post";
</style>
