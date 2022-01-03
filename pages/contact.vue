<template>
  <div class='main'>
    <Header />
    <div class='header-title'>
      <h1 class='big-text'>
        <span class="typed-text">{{ typeValueMain }}</span>
        <span class="cursor" :class="{'typing': typeStatusMain}">&nbsp;</span>
      </h1>
    </div>
    <div class='contact'>

      <div class='left-side-contact'>
        <h1 class='big-text small'>Wanna contact me? I'll be glad to receive any feedback! &#128233;</h1>
        <div class='left-side-contact-content'>
          <div class='contact-fields'>
            <input class='basic' placeholder='Email'>
            <input class='basic' placeholder='Title'>
            <textarea class='textarea' placeholder='Your message'/>
            <button class='ripple'>SEND</button>
          </div>
        </div>
        <h1 class='footer-note big-text small'>The message will be encrypted using my PGP public key
          (you can find it on the right side and send message manually).
          About how this was implemented you can find here!</h1>
      </div>

      <div class='right-side-contact'>
        <h1 class='big-text small'>Also, you can find me here. &#128206;</h1>
        <div class='top-items'>

          <div>
            <div v-for='(item) in copyValuesAndStatuses.slice(0, copyValuesAndStatuses.length - 3)' :key='item.name'>
              <span v-if='item.link' class='code-block code-block-hover tooltip' @click='openInNewTab(`${item.name}`)'>
                {{item.name}}: {{item.value}}
                <span class="tooltiptext">Open a new tab</span>
                <img :src='item.img' :alt="item.name" width='18' height='18'>
              </span>
              <span v-else class='code-block code-block-hover tooltip' @click='copyToClipboard(`${item.name.split(" ")[0]}`)'>
                {{item.name}}: {{item.value}}
                <input :id='`${item.name.split(" ")[0]}`' type='hidden' :value='item.value'>
                <span v-if='!item.status' class="tooltiptext">Click to copy</span>
                <span v-else class="tooltiptext">Copied</span>
                <img :src='item.img' :alt="item.name">
              </span>
            </div>
          </div>

        </div>

        <div class='bottom-items'>
          <h1 class='big-text small'>In case if you like what I'm doing &#9749;</h1>
          <div v-for='(item, idx) in copyValuesAndStatuses.slice(copyValuesAndStatuses.length - 3)' :key='item.name'>
            <p>
              <span class='code-block code-block-hover tooltip' @click='copyToClipboard(`${item.name}`)'>
                {{item.name}}: {{item.value}}
                <img :src='item.img' :alt='item.name'>
                <input :id='`${item.name}`' type='hidden' :value='copyValuesAndStatuses[idx + copyValuesAndStatuses.length - 3].value'>
                <span v-if='!copyValuesAndStatuses[idx + copyValuesAndStatuses.length - 3].status' class="tooltiptext">Click to copy</span>
                <span v-else class="tooltiptext">Copied</span>
              </span>
            </p>
          </div>
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

      copyValuesAndStatuses: [
        {name: 'Discord', value: 'bl4drnnr#6177', status: false, link: false, img: require('../assets/pics/discord.svg')},
        {name: 'HTB', value: 'bl4drnnr#691742', status: false, link: false, img: require('../assets/pics/htb.svg')},
        {name: 'PGP', value: '51E3 43BA 669A D317', status: false, link: true, img: require('../assets/pics/key.png')},
        {name: 'GitHub', value: 'github.com/Lain1wakura', status: false, link: true, img: require('../assets/pics/github.png')},
        {name: 'Offensive security', value: 'BL4DERUNNNER', status: false, link: false, img: require('../assets/pics/red_door.png')},
        {name: 'THM', value: 'tryhackme.com/p/BL4DERUNNNER', status: false, link: true, img: require('../assets/pics/thm.svg')},

        {name: 'LTC', value: 'LaxdwwKB6gBw2qzF8jrKRZwGstWN9UKK9b', status: false, img: require('../assets/pics/ltc.svg')},
        {name: 'BTC', value: 'bc1qmstcqe2k3vgzmx9rkn59fka9krk9p25ecjpqcc', status: false, img: require('../assets/pics/btc.svg')},
        {name: 'ETH', value: '0x05A892cc3DD63bDd9258073d8E9fB2512b0ee905', status: false, img: require('../assets/pics/eth.svg')},
      ],
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
    openInNewTab(link) {
      switch (link) {
        case "GitHub":
          window.open('https://github.com/Lain1wakura', '_blank')
          break
        case "PGP":
          window.open('https://keys.openpgp.org/search?q=51E3+43BA+669A+D317', '_blank')
          break
        case "THM":
          window.open('https://tryhackme.com/p/BL4DERUNNNER', '_blank')
          break
      }
    },
    copyToClipboard(id) {
      const copiedText = document.querySelector(`#${id}`)
      copiedText.setAttribute('type', 'text')
      copiedText.select()
      document.execCommand('copy');
      copiedText.setAttribute('type', 'hidden')
      window.getSelection().removeAllRanges()
      this.copyValuesAndStatuses.forEach(item => {
        item.status = item.name.split(" ")[0] === id;
      })
      setTimeout(() => {
        this.copyValuesAndStatuses.forEach(item => {
          item.status = false
        })
      }, 5000)
    },
  }
}
</script>

<style lang='scss'>
@import "assets/css/contact";
</style>
