<template>
  <div class='main'>
    <Header />
    <div class="content">
      <div class="center-text">
        <h1 class='big-text'>
          <span class="typed-text">{{ typeValueMain }}</span>
          <span class="cursor" :style="[showCursorMain ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusMain}">&nbsp;</span>
        </h1>
        <h1 class='big-text small'>
          <span class="typed-text">{{ typeValueSec }}</span>
          <span class="cursor" :style="[showCursorSec ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusSec}">&nbsp;</span>
        </h1>
      </div>
      <div class='bottom-text'>
        <h1 class='big-text smaller'>
          <span class="typed-text">{{ typeValueFooter }}</span>
          <span class="cursor" :style="[showCursorFooter ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusFooter}">&nbsp;</span>
        </h1>
      </div>
    </div>

    <div class="about">
      <div v-if='latestReleases.length > 0' class="left-about">
        <h1 class="title">Latest releases &#128293;</h1>

        <div v-for='item of latestReleases' :key='item.id'>
          <div class='post-preview home-page' @click='toPost(item.id, item.type)'>
            <div class='post-preview-img home-page-img' v-html='item.cover'></div>
            <div class='post-preview-content home-page-preview-content'>
              <p>{{ item.title }}</p>
              <p class='plot' v-html='item.plot'></p>
              <p class='date'>Posted at: {{ item.created_at }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="right-about">
        <h1 class="title">Let me explain who I am and what I do &#128163;</h1>
        <p>Mikhail Bahdashych aka <span class="code-block">bl4drnnr</span> | Pentester / Red Teamer wannabe. &#128165;</p>
        <p><span class='paragraph-begin'>Hello</span> &#128075;! Welcome to Pentester's Notes Blog (pNb), my personal blog dedicated to computer and information security.
          Here you can find a lot of interesting staff (hope so) about IS and, mostly,
          offensive security, like CTF's walk through, IS articles, tips and
          writeups of hacking various machines. &#128161;</p>
        <p>
          <span class='paragraph-begin'>At</span> the moment I am working as a full stack web developer, but cybersecurity is my passion and I step by step getting into it.
          Also, I'm very interested in network technologies, DevOpsing and coding. &#128187;
        </p>
      </div>
    </div>

    <div class="about blog">
      <div class="left-about">
        <h1 class="title">Why are you reading this? &#129418;</h1>
        <p>
          <span class='paragraph-begin'>I</span> decided it would be a good practice for my front-end and DevOps skills from the one side, and from the second side, create page where I can write some staff about IS.
          As a result of my work and my hobby, you can see this blog. &#127919;
          By the way, this blog was created using JavaScript
          <img :src='require("../assets/pics/js.svg")' alt="JS">
          (Front-end - Vue.JS <img :src='require("../assets/pics/vuejs.svg")' alt='VueJS'>
          + NuxtJS <img :src='require("../assets/pics/nuxtjs.svg")' alt='Nuxt.js'>
          and back-end - Express.js
          <img :src='require("../assets/pics/expressjs.svg")' alt='express.js' class='ex'> )
        </p>
        <p>
          <span class='paragraph-begin'>Why</span> I created this blog? That's a good question! Haven't you found cybersecurity hard? Well, I have.
          So I decided that the best way to learn something is to start teaching it to others. And it makes sense. On the one hand, I will be able to improve my skills and share them with others, and on the other hand, I'll need to learn how to correctly and structurally convey my thoughts to others, and for this I need to understand the material.
          In fact, everyone wins &#128640;
        </p>
      </div>
      <div class="right-about">
        <h1 class='title'>Here is list of technologies and programming languages I work(-ed) with:</h1>
        <p>Programming languages, frameworks and technologies:</p>
        <div class='icons'>
          <span v-for='item in pics.slice(0, 5)' :key='item.alt'>
            <img :src='item.src' :alt='item.alt'>
          </span>
        </div>
        <div class='icons'>
          <span v-for='item in pics.slice(5, 12)' :key='item.alt'>
            <img v-if='item.alt !=="Express"' :src='item.src' :alt='item.alt'>
            <img v-else :src='item.src' :alt='item.alt' class='set-background'>
          </span>
        </div>
        <div class='icons'>
          <span v-for='item in pics.slice(12, 18)' :key='item.alt'>
            <img v-if='item.alt !=="Express"' :src='item.src' :alt='item.alt'>
          </span>
        </div>
      </div>
    </div>

    <Footer/>
  </div>
</template>

<script>
import moment from 'moment';
import { getLatestReleases } from '~/api';
import Header from '~/components/Header';
import Footer from '~/components/Footer';
import { typer } from '~/mixins/typer';
export default {
  components: {
    Header,
    Footer
  },
  mixins: [typer],
  data() {
    return {
      pics: [
        {src: require('../assets/pics/js.svg'), alt: 'JS'},
        {src: require('../assets/pics/c++.svg'), alt: 'C++'},
        {src: require('../assets/pics/c-sharp.svg'), alt: 'C#'},
        {src: require('../assets/pics/python.svg'), alt: 'Python'},
        {src: require('../assets/pics/java.svg'), alt: 'Java'},
        {src: require('../assets/pics/vuejs.svg'), alt: 'VueJS'},
        {src: require('../assets/pics/nuxtjs.svg'), alt: 'Nuxt'},
        {src: require('../assets/pics/reactjs.svg'), alt: 'React'},
        {src: require('../assets/pics/angular.svg'), alt: 'Angular'},
        {src: require('../assets/pics/springio.svg'), alt: 'Spring'},
        {src: require('../assets/pics/expressjs.svg'), alt: 'Express'},
        {src: require('../assets/pics/netcore.svg'), alt: '.NET Core'},
        {src: require('../assets/pics/docker.svg'), alt: 'Docker'},
        {src: require('../assets/pics/nodejs.svg'), alt: 'Node.js'},
        {src: require('../assets/pics/mssql.svg'), alt: 'MsSQL'},
        {src: require('../assets/pics/mongodb.svg'), alt: 'Mongo'},
        {src: require('../assets/pics/mysql.svg'), alt: 'MySQL'},
        {src: require('../assets/pics/postgresql.svg'), alt: 'PostgreSQL'}
      ],

      latestReleases: [],
    }
  },
  async created() {
    setTimeout(this.typeTextMain, this.newTextDelayMain + 200);
    this.latestReleases = await getLatestReleases(3)
    Object.keys(this.latestReleases).forEach(x => { this.latestReleases[x].created_at = moment(this.latestReleases[x].created_at).format('YYYY-MM-DD HH:mm:ss') })
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
