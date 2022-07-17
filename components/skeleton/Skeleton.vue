<template>
  <div class="skeleton" :style="[width !== 0 ? {'width': `${width}px`} : {}]">
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
    },
    width: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/skeleton/Skeleton";
</style>
