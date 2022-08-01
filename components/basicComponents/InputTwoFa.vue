<template>
  <div :class="onwhite ? 'on-white' : ''">
    <input
      :id="`n1`"
      ref="n1"
      v-model="n1"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="this.nextElementSibling.focus()"
      @keyup.delete="clearTwoFa"
    >
    <input
      :id="`n2`"
      ref="n2"
      v-model="n2"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="this.nextElementSibling.focus()"
      @keyup.delete="clearTwoFa"
    >
    <input
      :id="`n3`"
      ref="n3"
      v-model="n3"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="this.nextElementSibling.focus()"
      @keyup.delete="clearTwoFa"
    >
    <input
      :id="`n4`"
      ref="n4"
      v-model="n4"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="this.nextElementSibling.focus()"
      @keyup.delete="clearTwoFa"
    >
    <input
      :id="`n5`"
      ref="n5"
      v-model="n5"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="this.nextElementSibling.focus()"
      @keyup.delete="clearTwoFa"
    >
    <input
      :id="`n6`"
      ref="n6"
      v-model="n6"
      :class="disabled ? `input-two-fa disabled`: `input-two-fa`"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      @keyup.delete="clearTwoFa"
    >
  </div>
</template>

<script>
import { validate2fa } from "~/helpers/frontValidator";
export default {
  name: "InputTwoFa",
  props: {
    disabled: {
      type: Boolean,
      default: false
    },
    onwhite: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      code: [
        { n1: '' }, { n2: '' }, { n3: '' }, { n4: '' }, { n5: '' }, { n6: '' }
      ],
      n1: '', n2: '', n3: '', n4: '', n5: '', n6: '',
      twoFaCode: ['', '', '', '', '', '']
    }
  },
  watch: {
    n1() {
      this.n1 = validate2fa(this.n1);
      this.twoFaCode[0] = this.n1;
      this.returnTwoFa()
    },
    n2() {
      this.n2 = validate2fa(this.n2);
      this.twoFaCode[1] = this.n2;
      this.returnTwoFa()
    },
    n3() {
      this.n3 = validate2fa(this.n3);
      this.twoFaCode[2] = this.n3;
      this.returnTwoFa()
    },
    n4() {
      this.n4 = validate2fa(this.n4);
      this.twoFaCode[3] = this.n4;
      this.returnTwoFa()
    },
    n5() {
      this.n5 = validate2fa(this.n5);
      this.twoFaCode[4] = this.n5;
      this.returnTwoFa()
    },
    n6() {
      this.n6 = validate2fa(this.n6);
      this.twoFaCode[5] = this.n6;
      this.returnTwoFa()
    }
  },
  methods: {
    returnTwoFa() {
      const normalCode = this.twoFaCode.join('')
      this.$emit('update:returnTwoFa', normalCode)
    },
    clearTwoFa() {
      this.n1 = ''
      this.n2 = ''
      this.n3 = ''
      this.n4 = ''
      this.n5 = ''
      this.n6 = ''
      this.$refs.n1.focus()
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/InputTwoFa";
</style>
