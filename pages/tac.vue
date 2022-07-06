<template>
  <div></div>
</template>

<script>
export default {
  name: "Tac",
  data() {
    return {
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  }
}
</script>

<style scoped>

</style>
