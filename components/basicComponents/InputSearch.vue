<template>
  <div class="basic-input-container">
    <input
      v-model="inputString"
      placeholder="Search..."
      class="bi bi--search"
    >
    <div v-if="showResult" class="bi--search__search-result"></div>
  </div>
</template>

<script>
export default {
  name: 'InputSearch',
  data() {
    return {
      inputString: '',
      showResult: false
    }
  },
  watch: {
    inputString() {
      this.showResult = this.inputString.length > 0
    }
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/Input";
</style>
