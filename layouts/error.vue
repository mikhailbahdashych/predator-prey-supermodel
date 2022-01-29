<template>
  <div>
    <div v-if='loading'></div>
    <div v-else>
      <h1>You shouldn't be here! >:(</h1>
      <p>
        <nuxt-link class='nuxt-link' to='/'>
          Go
        </nuxt-link>
        and find some cool staff out of here!
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loading: true
    }
  },
  head() {
    return {
      bodyAttrs: {
        class: 'reset-body-error'
      }
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.loading = false
    })
  }
}
</script>

<style lang='scss'>
.reset-body-error {
  text-align: center;
  color: white;
  font-size: 16px;
  h1, p {
    font-family: "Lato", sans-serif;
  }
  h1 {
    font-size: 52px;
  }
  p {
    font-size: 28px;
  }
  .nuxt-link {
    color: #69BEEB;
  }
}
</style>
