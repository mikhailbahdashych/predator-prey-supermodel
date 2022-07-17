<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'Blog',
  components: {
  },
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
@import "../../assets/css/pages/blog";
</style>
