<template>
  <div class='side-bar'>
    <nuxt-link to="/" style="text-decoration: none; color: white; text-align: center;"><h1>pNb</h1></nuxt-link>
    <div class='side-bar-menu'>
      <h3>Articles</h3>
      <h3>Write-ups</h3>
      <h3>Tips</h3>
      <h3>CTF's</h3>
      <hr>
      <p>Filter by dates</p>
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
