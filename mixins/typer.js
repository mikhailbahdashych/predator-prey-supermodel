export const typer = {
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
    }
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
  }
}
