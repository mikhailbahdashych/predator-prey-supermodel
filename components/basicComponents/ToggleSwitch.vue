<template>
  <div>
    <label class="switch">
      <input
        type="checkbox"
        :checked="value"
        @change="changeSwitch"
      >
      <span class="slider round" />
      <img
        :src="require('../../assets/img/sun.svg')"
        class="toggle-img"
        alt="moon"
        width="18"
        height="18"
      >
      <img
        :src="require('../../assets/img/moon.svg')"
        class="toggle-img right"
        alt="moon"
        width="18"
        height="18"
      >
    </label>
  </div>
</template>

<script>
export default {
  name: 'ToggleSwitch',
  props: {
    value: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      test: false
    }
  },
  methods: {
    changeSwitch() {
      this.$emit('input', !this.value);
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/ToggleSwitch";
</style>
