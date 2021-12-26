<template>
  <div class='main'>
    <Header />
    <div class="content">
      <div class="center-text">
        <h1>
          <span class="typed-text">{{ typeValueMain }}</span>
          <span class="cursor" :style="[showCursorMain ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusMain}">&nbsp;</span>
        </h1>
        <h1 style="font-size: 22px">
          <span class="typed-text">{{ typeValueSec }}</span>
          <span class="cursor" :style="[showCursorSec ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusSec}">&nbsp;</span>
        </h1>
      </div>
      <div style='margin-top: 100px'>
        <h1 style="font-size: 18px">
          <span class="typed-text">{{ typeValueFooter }}</span>
          <span class="cursor" :style="[showCursorFooter ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusFooter}">&nbsp;</span>
        </h1>
      </div>
    </div>

    <div class="about">
      <div v-if='latestReleases.length > 0' class="left-about">
        <h1 class="title">Latest releases &#128293;</h1>

        <div v-for='item of latestReleases' :key='item.id'>
          <div class='latest-releases' @click='toPost(item.title)'>
            <div class='latest-release-img'></div>
            <div class='latest-release-content'>
              <p>{{ item.title }}</p>
            </div>
          </div>
        </div>

      </div>
      <div class="right-about">
        <h1 class="title">Let me explain who I am and what I do &#128163;</h1>
        <p>Mikhail Bahdashych aka <span class="code-block">bl4drnnr</span> | Pentester / Red Teamer wannabe. &#128165;</p>
        <p><span style='margin-left: 3em'>Hello</span> &#128075;! Welcome to Pentester's Notes Blog (pNb), my personal blog dedicated to computer and information security.
          Here you can find a lot of interesting staff (hope so) about IS and, mostly,
          offensive security, like CTF's walk through, IS articles, tips and
          writeups of hacking various machines. &#128161;</p>
        <p>
          <span style='margin-left: 3em'>At</span> the moment I am working as a full stack web developer, but cybersecurity is my passion and I step by step getting into it.
          Also, I'm very interested in network technologies, DevOpsing and coding. &#128187;
        </p>
      </div>
    </div>

    <div class="about blog">
      <div class="left-about">
        <h1 class="title">Why are you reading this? &#129418;</h1>
        <p>
          <span style='margin-left: 3em'>I</span> decided it would be a good practice for my front-end and DevOps skills from the one side, and from the second side, create page where I can write some staff about IS.
          As a result of my work and my hobby, you can see this blog. &#127919;
          By the way, this blog was created using JavaScript <img src='../assets/pics/icons8-javascript.svg' alt='JS' width='22' height='22'>
          (Front-end - Vue.JS <img src='../assets/pics/icons8-vue-js.svg' alt='VueJS' width='22' height='22'>
          + NuxtJS <img src='../assets/pics/nuxtjs-icon.svg' alt='Nuxt.js' width='22' height='22'>
          and back-end - Express.js
          <span style='display: inline-flex; background-color: white; border-radius: 3px'>
              <img src='../assets/pics/expressjs-ar21.svg' alt='express.js' height='22' width='44'>
          </span> )
        </p>
        <p>
          <span style='margin-left: 3em'>Why</span> I created this blog? That's a good question! Haven't you found cybersecurity hard? Well, I have.
          So I decided that the best way to learn something is to start teaching it to others. And it makes sense. On the one hand, I will be able to improve my skills and share them with others, and on the other hand, I'll need to learn how to correctly and structurally convey my thoughts to others, and for this I need to understand the material.
          In fact, everyone wins &#128640;
        </p>
      </div>
      <div class="right-about">
        <h1 class='title'>Here is list of technologies and programming languages I work(-ed) with:</h1>
        <p>Programming languages, frameworks and technologies:</p>
        <div class='icons'>
          <img src='../assets/pics/icons8-javascript.svg' alt='JS' width='65' height='65'>
          <img src='../assets/pics/icons8-c++.svg' alt='C++' width='65' height='65'>
          <img src='../assets/pics/icons8-c-sharp-logo.svg' alt='C#' width='65' height='65'>
          <img src='../assets/pics/python-5.svg' alt='Python' width='65' height='65'>
          <img src='../assets/pics/icons8-java.svg' alt='Java' width='65' height='65'>
        </div>
        <div class='icons'>
          <img src='../assets/pics/springio-icon.svg' alt='Spring' width='50' height='50' style='margin-top: 10px'>
          <img src='../assets/pics/icons8-vue-js.svg' alt='VueJS' width='65' height='65'>
          <img src='../assets/pics/nuxtjs-icon.svg' alt='Nuxt.js' width='65' height='65'>
          <img src='../assets/pics/reactjs-icon.svg' alt='React' width='65' height='65'>
          <img src='../assets/pics/expressjs-ar21.svg' alt='express.js' height='60' width='120' class='filter-white'>
        </div>
        <div class='icons'>
          <img src='../assets/pics/icons8-docker.svg' alt='Docker' width='65' height='65'>
          <img src='../assets/pics/icons8-node-js.svg' alt='Node.js' width='65' height='65'>
        </div>

        <p style='margin-top: 0'>IDE's and databases I use:</p>
        <div class='icons ides'>
          <img src="../assets/pics/DataGrip_icon.svg" alt="DataGrip logo." width='65' height='65'>
          <img src="../assets/pics/IntelliJ_IDEA_icon.svg" alt="IntelliJ IDEA logo." width='65' height='65'>
          <img src="../assets/pics/PyCharm_icon.svg" alt="PyCharm logo." width='65' height='65'>
          <img src="../assets/pics/WebStorm_icon.svg" alt="WebStorm logo." width='65' height='65'>
          <img src="../assets/pics/Rider_icon.svg" alt="Rider logo." width='65' height='65'>
        </div>
        <div class='icons'>
          <img src='../assets/pics/icons8-microsoft-sql-server.svg' alt='MsSQL' width='65' height='65'>
          <img src='../assets/pics/mongodb-icon.svg' alt='MongoDB' width='65' height='65'>
          <img src='../assets/pics/mysql-icon.svg' alt='MySQL' width='65' height='65'>
        </div>
      </div>
    </div>

    <Footer />
  </div>
</template>

<script>
import { getLatestReleases } from '~/api';
import Header from '~/components/Header';
import Footer from '~/components/Footer';
export default {
  components: {
    Header,
    Footer
  },
  data() {
    return {
      typeValueMain: '',
      typeStatusMain: false,
      typeArrayMain: ['THE FUTURE IS HERE. THE FUTURE IS NOW.'],
      typingSpeedMain: 100,
      erasingSpeedMain: 100,
      newTextDelayMain: 1000,
      typeArrayIndexMain: 0,
      charIndexMain: 0,
      showCursorMain: true,

      typeValueSec: '',
      typeStatusSec: false,
      typeArraySec: ['CYBERSECURITY - WEB DEVELOPMENT - NETWORK TECHNOLOGIES'],
      typingSpeedSec: 100,
      erasingSpeedSec: 100,
      newTextDelaySec: 1000,
      typeArrayIndexSec: 0,
      charIndexSec: 0,
      showCursorSec: false,

      typeValueFooter: '',
      typeStatusFooter: false,
      typeArrayFooter: ['PENTESTER\'S NOTES BLOG BY MIKHAIL BAHDASHYCH'],
      typingSpeedFooter: 100,
      erasingSpeedFooter: 100,
      newTextDelayFooter: 1000,
      typeArrayIndexFooter: 0,
      charIndexFooter: 0,
      showCursorFooter: false,

      latestReleases: []
    }
  },
  async created() {
    setTimeout(this.typeTextMain, this.newTextDelayMain + 200);
    this.latestReleases = await getLatestReleases(3)
  },
  methods: {
    typeTextMain() {
      if (this.charIndexMain < this.typeArrayMain[this.typeArrayIndexMain].length) {
        if (!this.typeStatusMain)
          this.typeStatusMain = true;
        this.typeValueMain += this.typeArrayMain[this.typeArrayIndexMain].charAt(this.charIndexMain);
        this.charIndexMain += 1;
        setTimeout(this.typeTextMain, this.typingSpeedMain);
      } else {
        this.showCursorMain = false;
        this.showCursorSec = true
        this.typeTextSec()
      }
    },
    typeTextSec() {
      if (this.charIndexSec < this.typeArraySec[this.typeArrayIndexSec].length) {
        if (!this.typeStatusSec)
          this.typeStatusSec = true;
        this.typeValueSec += this.typeArraySec[this.typeArrayIndexSec].charAt(this.charIndexSec);
        this.charIndexSec += 1;
        setTimeout(this.typeTextSec, this.typingSpeedSec);
      } else {
        this.typeStatusSec = false;
        this.showCursorSec = false;
        this.showCursorFooter = true;
        this.typeFooterText();
      }
    },
    typeFooterText() {
      if (this.charIndexFooter < this.typeArrayFooter[this.typeArrayIndexFooter].length) {
        if (!this.typeStatusFooter)
          this.typeStatusFooter = true;
        this.typeValueFooter += this.typeArrayFooter[this.typeArrayIndexFooter].charAt(this.charIndexFooter);
        this.charIndexFooter += 1;
        setTimeout(this.typeFooterText, this.typingSpeedFooter);
      } else {
        this.typeStatusFooter = false;
        this.showCursorFooter = true;
      }
    }
  },
}
</script>

<style lang='scss'>
@import "../assets/css/homepage";
</style>
