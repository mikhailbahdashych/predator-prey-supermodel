<template>
  <div @click="clickHandler">
    <button
      class="basic-button"
      :disabled="disabled"
      :class="additionalClass"
      @click="$emit('click-handler')"
    >
      <p class="label">{{ label }}</p>
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
