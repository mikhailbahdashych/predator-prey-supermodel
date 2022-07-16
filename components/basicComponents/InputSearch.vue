<template>
  <div class="basic-input-container">
    <input
      placeholder="Search..."
      class="bi search"
      :value="inputString"
    >
  </div>
</template>

<script>
export default {
  name: 'InputSearch',
  data() {
    return {
      inputString: ''
    }
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/Input";
</style>
