<template>
  <div>

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
