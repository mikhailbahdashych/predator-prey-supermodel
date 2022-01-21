<template>
  <div class='blog-header'>
    <div class='search-div'>
      <input v-model='searchInput' class='basic-input search-field' placeholder='Search...'>
    </div>
    <div v-if='searchInput && result.length > 0' class='search-box'>
      <div v-if='localLoader'>
        Loading...
      </div>
      <div v-if='showInputError'>
        <p>Only letters and number allowed!</p>
      </div>
      <div v-else>
        <div v-if='searchInput && searchInput.length'>
          <div v-for='post in result' :key='post.id'>
            <div class='post-box' @click='toPost(post.id, post.type)'>
              <div v-if='post.type === "tip"'><p style='color: #8CC271'>[{{ post.type.toUpperCase() }}]</p></div>
              <div v-if='post.type === "ctf"'><p style='color: #F5AA39'>[{{ post.type.toUpperCase() }}]</p></div>
              <div v-if='post.type === "article"'><p style='color: #69BEEB'>[{{ post.type.toUpperCase() }}]</p></div>
              <div v-if='post.type === "writeup"'><p style='color: #E9643B'>[{{ post.type.toUpperCase() }}]</p></div>
              <p>{{ post.title }}</p>
            </div>
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
      // @TODO do loader
      this.showInputError = false
      const validInput = this.inputRegex.test(this.searchInput)

      if (this.searchInput && !validInput) {
        this.showInputError = true
        this.localLoader = false
        return
      }
      if (this.searchInput.length > 1) {
        this.result = await search({
          input: this.searchInput
        })
      }
      this.localLoader = false
    },
    toPost(id, type) {
      this.$router.push({
        path: `${type + 's'}/${id}`
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../assets/css/search";
</style>
