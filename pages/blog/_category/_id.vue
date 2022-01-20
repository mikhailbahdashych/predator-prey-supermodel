<template>
  <div>
    <SideBar :subpages='subpages' @clicked="getPostsByCategory" />
    <Search />
    <div class='post-content'>
      <div v-if='$route.params.id' class='content-body'>
        <h1 class='big-text post-title'>{{ post.title }}</h1>
        <div v-html='post.text'></div>
      </div>
      <div v-else>
        <div v-if='loading'>
          <p class='skeleton-text skeleton-header'></p>
          <div v-for='i of 3' :key='i'>
            <p class='skeleton-text plot skeleton-text-centered'></p>
          </div>
        </div>
        <div v-if='!loading'>
          <div v-for='title in categoriesAndPretitles' :key='title.section'>
            <div v-if='$route.params.category === title.section'>
              <h1 class='big-text post-title'>{{title.title}}</h1>
              <p class='description-text'>{{title.text}}</p>
            </div>
          </div>
        </div>
        <PostsListsSkeleton v-if='loading' q="5" />

        <div v-if='!loading'>
          <div v-for='p of posts' :key='p.id'>
            <div class='post-preview' @click='toPost(p.id, p.type)'>
              <div class='post-preview-img' v-html='p.cover'></div>
              <div class='post-preview-content'>
                <p>{{ p.title }}</p>
                <p class='plot' v-html='p.plot'></p>
                <p class='date'>Posted at: {{ p.created_at }}</p>
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
import moment from 'moment';
import hljs from 'highlight.js/lib/core';
import javascript from 'highlight.js/lib/languages/javascript';
import html from 'highlight.js/lib/languages/xml';
import csharp from 'highlight.js/lib/languages/csharp';

import { getPostById, getPostsByCategory } from '~/api';
import Footer from '~/components/Footer';
import SideBar from '~/components/SideBar';
import Search from '~/components/Search';
import PostsListsSkeleton from '~/components/Skeletons/PostsListsSkeleton';

import 'highlight.js/styles/github-dark-dimmed.css';
hljs.registerLanguage('javascript', javascript);
hljs.registerLanguage('html', html);
hljs.registerLanguage('csharp', csharp);
export default {
  name: 'Index',
  components: {
    Footer,
    SideBar,
    Search,
    PostsListsSkeleton
  },
  data() {
    return {
      post: {},
      posts: [],
      typeOfPosts: null,
      categories: ['articles', 'writeups', 'tips', 'ctfs'],
      categoriesAndPretitles: [{
        section: 'articles',
        title: 'Here is list of all articles and news posts',
        text: '\tA section with the widest range of topics. Here you can find topics from programming, and in particular web development, to cybersecurity and DevOpsing. Also, here I try to write not only articles, but also various news from the world of high technologies.'
      }, {
        section: 'writeups',
        title: 'Write-ups and machines walkthroughs',
        text: '\tA section with pure practical knowledge of hacking machines. There will be not only machines with known resources, but also, for example, virtual machines with viruses or test lockers.'
      }, {
        section: 'ctfs',
        title: 'Capture the flag competitions',
        text: '\tCTF (Capture The Flag) is a kind of information security competition that challenges contestants to solve a variety of tasks ranging from a scavenger hunt on wikipedia to basic programming exercises, to hacking your way into a server to steal data. In these challenges, the contestant is usually asked to find a specific piece of text that may be hidden on the server or behind a webpage. This goal is called the flag, hence the name!'
      }, {
        section: 'tips',
        title: 'Little tips about IS and IT in general',
        text: '\tSmall tips and tricks related not only to cybersecurity, but also to IT in general. Here will be described simple things that you just would like to keep on hand and take a look at them if necessary or if you forgot about something.'
      }],
      subpages: [
        {name: 'Blog main page', value: 'bmp', page: '/blog', status: false},
        {name: 'Articles', value: 'article', page: '/blog/articles', status: false},
        {name: 'Write-ups', value: 'writeup', page: '/blog/writeups', status: false},
        {name: 'Tips', value: 'tip', page: '/blog/tips', status: false},
        {name: 'CTF\'s', value: 'ctf', page: '/blog/ctfs', status: false},
      ],
      loading: true
    }
  },
  mounted() {
    this.$nextTick(async () => {
      this.getAndCheckCategory()
      if (this.$route.params.id) await this.getPostById()
      else await this.getPostsByCategory()

      document.querySelectorAll('pre.ql-syntax').forEach(el => {
        hljs.highlightElement(el);
      })
      this.loading = false
    })
  },
  methods: {
    async getPostById() {
      this.post = await getPostById(this.$route.params.id)
    },
    async getPostsByCategory(value) {
      let dates = { from: null, to: null }
      if (value) dates = { from: value[0], to: value[1] }
      this.posts = await getPostsByCategory({ category: this.typeOfPosts, from: dates.from, to: dates.to })
      Object.keys(this.posts).forEach(x => { this.posts[x].created_at = moment(this.posts[x].created_at).format('YYYY-MM-DD HH:mm:ss') })
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
    },
    toPost(id, type) {
      this.$router.push({
        path: `/blog/${type + 's'}/${id}`
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../../../assets/css/post";
@import "../../../assets/css/blog";
@import "../../../assets/css/search";
</style>
