<template>
  <div>
    <div v-for='item in parseInt(q)' :key='item'>
      <div class='post-preview skeleton'>
        <div class='post-preview-img skeleton-img'></div>
        <div class='post-preview-content'>
          <p class='skeleton-text'></p>
          <p class='skeleton-text plot'></p>
          <p class='skeleton-text plot'></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostsListsSkeleton',
  props: { 'q': {type: String, required: true} },
}
</script>

<style lang='scss'>
@import "../../assets/css/main";
</style>
