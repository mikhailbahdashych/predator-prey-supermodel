<template>
  <div class='blog-header'>
    <div class='search-div'>
      <input v-model='searchInput' class='basic-input search-field' placeholder='Search...'>
    </div>
    <div v-if='searchInput' class='search-box'>
      <div v-if='localLoader'>
        Loading...
      </div>
      <div v-if='showInputError'>
        <p>Only letters and number allowed!</p>
      </div>
      <div v-else>
        <div v-if='searchInput && searchInput.length'>
          <div v-for='post in result' :key='post.id'>
            <p>{{ post.title }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { search } from '~/api';
export default {
  name: 'Search',
  data() {
    return {
      searchInput: '',
      showInputError: false,
      showShadow: false,
      // eslint-disable-next-line prefer-regex-literals
      inputRegex: RegExp('^[a-zA-Z0-9 ]*$'),
      result: [],
      localLoader: false
    }
  },
  watch: {
    searchInput() {
      this.localLoader = true
      this.search()
    }
  },
  methods: {
    async search() {
      this.showInputError = false
      const validInput = this.inputRegex.test(this.searchInput)

      if (this.searchInput && !validInput) {
        this.showInputError = true
        this.localLoader = false
        return
      }
      if (this.searchInput.length > 2) {
        this.result = await search({
          input: this.searchInput
        })
      }
      this.localLoader = false
    }
  }
}
</script>

<style lang='scss'>
@import "../assets/css/search";
</style>
