<template>
  <div :class="onwhite ? 'on-white' : ''">
    <input
      :id="`n1`"
      v-model="i1"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { if (this.previousElementSibling) {this.previousElementSibling.focus()} } else { this.nextElementSibling.focus() }"
    >
    <input
      :id="`n2`"
      v-model="i2"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { this.previousElementSibling.focus() } else { this.nextElementSibling.focus() }"
    >
    <input
      :id="`n3`"
      v-model="i3"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { this.previousElementSibling.focus() } else { this.nextElementSibling.focus() }"
    >
    <input
      :id="`n4`"
      v-model="i4"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { this.previousElementSibling.focus() } else { this.nextElementSibling.focus() }"
    >
    <input
      :id="`n5`"
      v-model="i5"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { this.previousElementSibling.focus() } else { this.nextElementSibling.focus() }"
    >
    <input
      :id="`n6`"
      v-model="i6"
      class="input-two-fa center"
      type="number"
      :disabled="disabled"
      min="0"
      max="9"
      autocomplete="off"
      autofocus
      oninput="if (this.value === '') { this.previousElementSibling.focus() } else { if (this.nextElementSibling) { this.nextElementSibling.focus() } }"
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
      i1: '', i2: '', i3: '', i4: '', i5: '', i6: '',
      twoFaCode: ['', '', '', '', '', '']
    }
  },
  watch: {
    i1() { this.i1 = validate2fa(this.i1); this.twoFaCode[0] = this.i1; this.returnTwofa() },
    i2() { this.i2 = validate2fa(this.i2); this.twoFaCode[1] = this.i2; this.returnTwofa() },
    i3() { this.i3 = validate2fa(this.i3); this.twoFaCode[2] = this.i3; this.returnTwofa() },
    i4() { this.i4 = validate2fa(this.i4); this.twoFaCode[3] = this.i4; this.returnTwofa() },
    i5() { this.i5 = validate2fa(this.i5); this.twoFaCode[4] = this.i5; this.returnTwofa() },
    i6() { this.i6 = validate2fa(this.i6); this.twoFaCode[5] = this.i6; this.returnTwofa() },
  },
  methods: {
    returnTwofa() {
      this.$emit('returnTwofa', this.twoFaCode)
    },
  }
}
</script>

<style lang="scss">
@import "../assets/css/components/InputTwoFa";
</style>
