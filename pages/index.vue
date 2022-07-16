<template>
  <div>

  </div>
</template>

<script>
export default {
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
