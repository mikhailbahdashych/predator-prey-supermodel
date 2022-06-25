<template>
  <div @click="clickOn">
    <button
      class="basic-button"
      :disabled="disabled"
      :class="additionalClass"
    >
      <p>{{ label }}</p>
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
@import "../assets/css/components/Button";
</style>
