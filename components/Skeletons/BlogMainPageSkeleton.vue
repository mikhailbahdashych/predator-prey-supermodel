<template>
  <div class='container-block'>
    <div class='items'>
      <div v-for='post of 2' :key='post' class='post-preview main-page-blog'>
        <div class='post-preview-img skeleton-img'></div>
        <div class='post-preview-content main-page-blog-preview-content'>
          <p class='skeleton-text'></p>
          <div v-for='i of 3' :key='i'>
            <p class='plot skeleton-text'></p>
          </div>
        </div>
      </div>
    </div>
    <div class='items'>
      <div v-for='post of 2' :key='post' class='post-preview main-page-blog'>
        <div class='post-preview-img skeleton-img'></div>
        <div class='post-preview-content main-page-blog-preview-content'>
          <p class='skeleton-text'></p>
          <div v-for='i of 3' :key='i'>
            <p class='plot skeleton-text'></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogMainPageSkeleton'
}
</script>

<style lang='scss'>
@import "../../assets/css/blog";
@import "../../assets/css/search";
</style>
