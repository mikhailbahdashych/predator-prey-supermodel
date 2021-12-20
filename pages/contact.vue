<template>
  <div class='main'>
    <Header />
    <div class='contact'>

      <div class='left-side-contact'>
        <h1>Wanna contact me? I'll be glad to receive any feedback!</h1>
        <div class='left-side-contact-content'>
          <div class='contact-fields'>
            <input class='basic' placeholder='Email'>
            <input class='basic' placeholder='Title'>
            <textarea class='textarea' placeholder='Your message'/>
          </div>
        </div>
      </div>

      <div class='right-side-contact'>
        <h1>Also, you can find me here.</h1>
        <div class='top-items'>
          <div class='left-side'>
            <p>Feel free to click on icons to copy</p>
            <span class='code-block'>Discord: bl4drnnr#6177
              <img src='../assets/pics/Discord-Logo-White.svg' alt='Discord' width='18' height='18'>
            </span>
            <span class='code-block'>PGP: A0F3 A1A5 A32E 3378 &#128273;</span>
          </div>
          <div class='right-side'>
            <p>Links to my profiles</p>
            <p><span class='code-block'>My profiles at: HTB, TMH, OS, Github &#128206;</span></p>
          </div>
        </div>
        <div class='bottom-items'>
          <p>In case if you like what I'm doing<img src='../assets/pics/coffee-emoji-by-google.png' alt='coffee' width='20' height='20' style='vertical-align: middle'></p>
          <span class='code-block'>BTC: bc1qmstcqe2k3vgzmx9rkn59fka9krk9p25ecjpqcc</span>
          <span class='code-block'>ETH: 0x05A892cc3DD63bDd9258073d8E9fB2512b0ee905</span>
          <span class='code-block'>LTC: LaxdwwKB6gBw2qzF8jrKRZwGstWN9UKK9b</span>
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

    }
  }
}
</script>

<style lang='scss'>
@import "assets/css/contact";
</style>
