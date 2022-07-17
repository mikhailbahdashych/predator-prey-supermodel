<template>
  <div></div>
</template>

<script>
export default {
  name: 'CreateThread',
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

<style scoped>

</style>
