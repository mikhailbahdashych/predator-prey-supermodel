<template>
  <div>
    <div class="account-preferences">

    </div>
  </div>
</template>

<script>
export default {
  name: 'SiteSettings',
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

<style lang="scss">
@import "../../../assets/css/pages/account/settings";
</style>
