<template>
  <div class='main'>
    <div class="content">
      <div class="center-text">
      </div>
    </div>

    <div class="about">
    </div>

    <div class="about blog">
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true,
      latestReleases: [],
    }
  },
  head() {
    return {
    }
  },
  methods: {
    toPost(id, type) {
      this.$router.push({
        path: `blog/${type + 's'}/${id}`
      })
    },
  },
}
</script>

<style lang='scss'>
@import "../assets/css/homepage";
</style>
