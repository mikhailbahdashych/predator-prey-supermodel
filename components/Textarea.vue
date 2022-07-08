<template>
  <div class="basic-textarea-outer">
    <p :class="`paragraph`">{{ title }}</p>
    <textarea class="bi textarea" />
  </div>
</template>

<script>
export default {
  name: "Textarea",
  props: {
    title: {
      type: String,
      default: ''
    },
  }
}
</script>

<style lang="scss">
@import "../assets/css/components/Input";
</style>
