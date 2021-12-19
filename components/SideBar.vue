<template>
  <div class='side-bar'>
    <nuxt-link to="/" style="text-decoration: none; color: white; text-align: center;"><h1>pNb</h1></nuxt-link>
    <div class='side-bar-menu'>
      <ul>
        <li><span class="underline-text"><a class='link-href'>Articles</a></span></li>
        <li><span class="underline-text"><a class='link-href'>Write-ups</a></span></li>
        <li><span class="underline-text"><a class='link-href'>Tips</a></span></li>
        <li><span class="underline-text"><a class='link-href'>CTF's</a></span></li>
      </ul>
      <div class='filters'>
        <p>Filter by dates:</p>
        <label for="start">Start date:</label>
        <input id="start" type="date" name="trip-start"
               value="2018-07-22"
               min="2018-01-01" max="2018-12-31">
        <button @click='test()'>FILTER</button>
      </div>
    </div>
  </div>
</template>

<script>
import { getArticles } from '~/api';
export default {
  name: 'SideBar',
  data() {
    return {

    }
  },
  methods: {
    async test() {
      const data = await getArticles();
      console.log(data)
    }
  }
}
</script>

<style lang='scss'>
@import "assets/css/sideBar";
</style>
