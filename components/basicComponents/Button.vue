<template>
  <div class="button-container" @click="clickHandler">
    <button
      class="basic-button"
      :disabled="disabled"
      :class="btnClass"
      @click="$emit('click-handler')"
    >
      <p class="basic-button__label">{{ label }}</p>
    </button>
  </div>
</template>

<script>
export default {
  name: "Button",
  props: {
    label: {
      type: String,
      default: ''
    },
    disabled: {
      type: Boolean,
      default: false
    },
    clickHandler: {
      type: Function,
      default: () => {}
    },
    btnClass: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/Button";
</style>
