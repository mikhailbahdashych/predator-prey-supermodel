<template>
  <div class="skeleton">
    <p class="skeleton-text">{{ text }}</p>
  </div>
</template>

<script>
export default {
  name: "SkeletonText",
  props: {
    text: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/skeleton/Skeleton";
</style>
