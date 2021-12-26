<template>
  <div class='main'>
    <Header />
    <div class='header-title'>
      <h1>
        <span class="typed-text">{{ typeValueMain }}</span>
        <span class="cursor" :class="{'typing': typeStatusMain}">&nbsp;</span>
      </h1>
    </div>
    <div class='contact'>

      <div class='left-side-contact'>
        <h1>Wanna contact me? I'll be glad to receive any feedback! &#128233;</h1>
        <div class='left-side-contact-content'>
          <div class='contact-fields'>
            <input class='basic' placeholder='Email'>
            <input class='basic' placeholder='Title'>
            <textarea class='textarea' placeholder='Your message'/>
            <button class='send-btn'>SEND</button>
          </div>
        </div>
        <h1 class='footer-note'>The message will be encrypted using my PGP public key
          (you can find it on the right side and send message manually).
          About how this was implemented you can find here!</h1>
      </div>

      <div class='right-side-contact'>
        <h1>Also, you can find me here. &#128206;</h1>
        <div class='top-items'>
          <div>
            <div>
              <span class='code-block code-block-hover'>Discord: bl4drnnr#6177
                <img src='../assets/pics/Discord-Logo-White.svg' alt='Discord' width='18' height='18'>
              </span>
            </div>
            <div>
              <span class='code-block code-block-hover'>PGP: A0F3 A1A5 A32E 3378 &#128273;</span>
            </div>
            <div>
              <span class='code-block code-block-hover'>GitHub: github.com/Lain1wakura
                <img src='../assets/pics/GitHub-Mark-120px-plus.png' alt='GitHub' width='18' height='18'>
              </span>
            </div>
            <div><span class='code-block code-block-hover'>
              THM: tryhackme.com/p/BL4DERUNNNER
              <img src='../assets/pics/thm.svg' alt='thm' style='vertical-align: middle'>
            </span></div>
            <div><span class='code-block code-block-hover'>Offensive security: BL4DERUNNNER &#128682;</span></div>
            <div><span class='code-block code-block-hover'>
              HTB: bl4drnnr#691742
              <img src='../assets/pics/hack-the-box-svgrepo-com.svg' alt='htb' width='18' height='18' style='vertical-align: middle'>
            </span></div>
          </div>
        </div>
        <div class='bottom-items'>
          <p style='margin-bottom: 25px'>In case if you like what I'm doing &#9749;</p>
          <p><span class='code-block code-block-hover'>BTC: bc1qmstcqe2k3vgzmx9rkn59fka9krk9p25ecjpqcc</span></p>
          <p><span class='code-block code-block-hover'>ETH: 0x05A892cc3DD63bDd9258073d8E9fB2512b0ee905</span></p>
          <p><span class='code-block code-block-hover'>LTC: LaxdwwKB6gBw2qzF8jrKRZwGstWN9UKK9b</span></p>
        </div>
      </div>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Header from '~/components/Header';
import Footer from '~/components/Footer'
export default {
  name: 'Contact',
  components: {
    Header,
    Footer
  },
  data() {
    return {
      typeValueMain: '',
      typeStatusMain: false,
      typeArrayMain: ['Let\'s make something awesome together!'],
      typingSpeedMain: 100,
      erasingSpeedMain: 100,
      newTextDelayMain: 1000,
      typeArrayIndexMain: 0,
      charIndexMain: 0,
    }
  },
  created() {
    setTimeout(this.typeTextMain, this.newTextDelayMain + 200);
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
        this.typeStatusMain = false;
      }
    },
  }
}
</script>

<style lang='scss'>
@import "assets/css/contact";
</style>
