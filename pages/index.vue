<template>
  <div>
    <div class="welcome welcome__pnb">
      <span class="welcome__intro welcome__intro--pnb">PENTESTERS' NOTES BLOG</span>
    </div>
    <div class="welcome">
      <span class="welcome__intro">
        WHERE WE MAKE <span class="welcome__intro--bold">IT</span> SECURE
      </span>
    </div>
  </div>
</template>

<script>
import theme from '~/mixins/theme'
export default {
  mixins: [theme],
  data() {
    return {
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
}
</script>

<style lang='scss'>
@import "../assets/css/pages/homepage";
</style>
