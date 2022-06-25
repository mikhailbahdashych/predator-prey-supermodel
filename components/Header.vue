<template>
  <div class="header">
    <div class="inner-header">
      <div class="header-content">
        <div class="header-content">
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links logo">pNb</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">FORUM</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">Q&A</h3>
          </nuxt-link>
          <nuxt-link to="/" class='nuxt-link'>
            <h3 class="header-links">BLOG</h3>
          </nuxt-link>
        </div>
        <div class="header-content">
          <div class="header-button">
            <Button :label="'SIGN IN'" :additional-class="'transparent'" />
          </div>
          <div class="header-button">
            <Button :label="'SIGN UP'" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Button from "~/components/Button";
export default {
  name: 'Header',
  components: {
    Button
  }
}
</script>

<style lang='scss'>
@import '../assets/css/Header';
</style>
