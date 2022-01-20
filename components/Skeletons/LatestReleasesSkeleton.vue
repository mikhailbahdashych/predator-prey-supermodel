<template>
  <div class='left-about'>
    <h1 class="title">Latest releases &#128293;</h1>
    <div v-for='item in parseInt(q)' :key='item'>
      <div class='post-preview home-page skeleton'>
        <div class='post-preview-img home-page-img skeleton-img'></div>
        <div class='post-preview-content home-page-preview-content'>
          <p class='skeleton-text'></p>
          <div v-for='i of 2' :key='i'>
            <p class='skeleton-text plot'></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LatestReleasesSkeleton',
  props: { 'q': {type: String, required: true} },
}
</script>

<style lang='scss'>
@import "../../assets/css/homepage";
</style>
