<template>
  <div></div>
</template>

<script>
export default {
  name: 'Index',
  layout: 'default',
  data() {
    return {
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/forum";
</style>
