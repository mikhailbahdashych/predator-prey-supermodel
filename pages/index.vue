<template>
  <div>
    <Header />
    <div class="content">
      <div class="center-text">
        <h1>
          <span class="typed-text">{{ typeValueMain }}</span>
          <span class="cursor" :class="{'typing': typeStatusMain}">&nbsp;</span>
        </h1>
        <h1 style="font-size: 22px">
          <span class="typed-text">{{ typeValueSec }}</span>
          <span class="cursor" :class="{'typing': typeStatusSec}">&nbsp;</span>
        </h1>
      </div>
    </div>

    <div class="about">
      <div class="left-about">
        <img src="../assets/pics/DataGrip_icon.svg" alt="DataGrip logo.">
        <img src="../assets/pics/IntelliJ_IDEA_icon.svg" alt="IntelliJ IDEA logo.">
        <img src="../assets/pics/PyCharm_icon.svg" alt="PyCharm logo.">
        <img src="../assets/pics/WebStorm_icon.svg" alt="WebStorm logo.">
        <img src="../assets/pics/Rider_icon.svg" alt="Rider logo.">
      </div>
      <div class="right-about">
        <h1 class="title">Let me explain who I am and what I do</h1>
        <p>Mikhail Bahdashych aka <span class="code-block">bl4drnnr</span> | Pentester / Red Teamer wannabe. &#128165;</p>
        <p><span style='margin-left: 3em'>Hello</span> &#128075;! Welcome to my personal blog dedicated to computer and information security.
          Here you can find a lot of interesting staff (hope so) about IS and, mostly,
          offensive security, like CTF's walk through, IS articles, tips and
          writeups of hacking various machines. &#128161;</p>
        <p>
          <span style='margin-left: 3em'>At</span> the moment I am working as a full stack web developer, but cybersecurity is my passion and I step by step getting into it.
          Also, I'm very interested in network technologies, DevOpsing and coding. &#128187;
        </p>
        <p><span style='margin-left: 3em'>Here</span> is list of technologies and programming languages I work(-ed) with:</p>
      </div>
    </div>

    <div class="about blog">
      <div class="left-about">
        <h1 class="title">Why are you reading this?</h1>
        <p>
          <span style='margin-left: 3em'>I</span> decided it would be a good practice for my front-end skills from the one side, and from the second side, create page where I can write some staff about IS.
          As a result of my work and my hobby, you can see this blog. &#127919;
        </p>
        <p>
          <span style='margin-left: 3em'>Why</span> I created this blog? That's a good question! Haven't you found cybersecurity hard? Well, I have.
          So I decided that the best way to learn something is to start teaching it to others. And it makes sense. On the one hand, I will be able to improve my skills and share them with others, and on the other hand, I'll need to learn how to correctly and structurally convey my thoughts to others, and for this I need to understand the material.
          In fact, everyone wins &#128640;
        </p>
      </div>
      <div class="right-about">
        <h1 class="title">Wanna contact me? I'll be glad to receive any feedback!</h1>
        <p>
            <span class='code-block'>Discord: bl4drnnr#6177
              <img src='../assets/pics/Discord-Logo-White.svg' alt='Discord' width='18' height='18'>
            </span>
        </p>
        <p>
          <span class='code-block'>PGP: A0F3 A1A5 A32E 3378 &#128273;</span>
        </p>
        <p><span class='code-block'>My profiles at: HTB, TMH, OS, Github &#128206;</span></p>
        <p>In case if you like what I'm doing <span><img src='../assets/pics/coffee-emoji-by-google.png' alt='coffee' width='20' height='20'></span></p>
        <p><span class='code-block'>BTC: bc1qmstcqe2k3vgzmx9rkn59fka9krk9p25ecjpqcc</span></p>
        <p><span class='code-block'>ETH: 0x05A892cc3DD63bDd9258073d8E9fB2512b0ee905</span></p>
        <p><span class='code-block'>LTC: LaxdwwKB6gBw2qzF8jrKRZwGstWN9UKK9b</span></p>
        &#127928;
        &#127929;
      </div>
    </div>

    <Footer />
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
      typeValueMain: '',
      typeStatusMain: false,
      typeArrayMain: ['THE FUTURE IS HERE. THE FUTURE IS NOW.'],
      typingSpeedMain: 100,
      erasingSpeedMain: 100,
      newTextDelayMain: 1000,
      typeArrayIndexMain: 0,
      charIndexMain: 0,

      typeValueSec: '',
      typeStatusSec: false,
      typeArraySec: ['CYBERSECURITY - WEB DEVELOPMENT - NETWORK TECHNOLOGIES'],
      typingSpeedSec: 100,
      erasingSpeedSec: 100,
      newTextDelaySec: 1000,
      typeArrayIndexSec: 0,
      charIndexSec: 0,
    }
  },
  created() {
    setTimeout(this.typeTextMain, this.newTextDelayMain + 200);
  },
  methods: {
    typeTextMain() {
      if(this.charIndexMain < this.typeArrayMain[this.typeArrayIndexMain].length) {
        if(!this.typeStatusMain)
          this.typeStatusMain = true;
        this.typeValueMain += this.typeArrayMain[this.typeArrayIndexMain].charAt(this.charIndexMain);
        this.charIndexMain += 1;
        setTimeout(this.typeTextMain, this.typingSpeedMain);
      } else {
        this.typeStatusMain = false;
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
      }
    }
  },
}
</script>

<style lang='scss'>
@import "assets/css/homePage";
</style>
