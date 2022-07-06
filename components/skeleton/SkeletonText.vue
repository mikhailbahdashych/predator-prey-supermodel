<template>
  <div class="skeleton-container">
    <p class="skeleton-text">{{ text }}</p>
  </div>
</template>

<script>
export default {
  props: {
    type: {
      type: String,
      default: ''
    },
    text: {
      type: String,
      default: ''
    }
  },
  name: "SkeletonText"
}
</script>

<style lang="scss">
@import "../../assets/css/components/SkeletonText";
</style>
