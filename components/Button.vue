<template>
  <div @click="clickOn">
    <button
      @click="$emit('show')"
      :disabled="disabled"
      class="basic-button"
      :class="additionalClass"
    >
      {{ label }}
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
    clickOn: {
      type: Function,
      default: () => {}
    },
    additionalClass: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/Button";
</style>
