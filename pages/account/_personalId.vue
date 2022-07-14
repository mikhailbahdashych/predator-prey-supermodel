<template>
  <div>

  </div>
</template>

<script>
export default {
  name: 'PersonalId',
  data() {
    return {
      user: {},
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
  },
  methods: {
  }
}
</script>

<style lang='scss'>
@import "../../assets/css/account";
</style>
