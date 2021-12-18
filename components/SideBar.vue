<template>
  <div class='side-bar'>
    <nuxt-link to="/" style="text-decoration: none; color: white"><h1>pNb</h1></nuxt-link>
    <div class='side-bar-menu'>
      <h3>Articles</h3>
      <h3>Write up's</h3>
      <h3>Tips</h3>
      <h3>CTF's</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SideBar'
}
</script>

<style lang='scss'>
@import "assets/css/sideBar";
</style>
