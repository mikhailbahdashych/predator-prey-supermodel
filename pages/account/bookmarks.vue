<template>
  <div class="bookmarks">
    <h1>Your bookmarks</h1>
    <div class="bookmarks__header">
      <p>Show: </p>
      <div v-for="f in filters" :key="f.value" class="bookmarks__sort-buttons">
        <p
          :class="`bookmarks__button bookmarks__button--${f.value} ${f.active ? 'active': ''}`"
          @click="filterBookmarks(f)"
        >{{ f.title }}</p>
      </div>
    </div>
    <div v-for="b in bookmarks" :key="b" class="bookmarks__content">
      <p>{{ b }}</p>
    </div>
  </div>
</template>

<script>
import { getBookmarks, getRefreshedTokens } from '~/api'
// import Skeleton from '~/components/skeleton/Skeleton'
export default {
  name: 'Bookmarks',
  components: {
    // Skeleton
  },
  layout: 'default',
  data() {
    return {
      loading: true,
      bookmarks: [],
      filters: [
        { title: 'Show all', value: 'all', active: true },
        { title: 'Questions', value: 'questions', active: false },
        { title: 'Forum threads', value: 'forum', active: false },
        { title: 'Blog posts', value: 'blog', active: false }
      ],
      filter: 'all'
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.getBookmarks()
  },
  methods: {
    filterBookmarks(filter) {
      this.filters.forEach(f => { f.active = f.value === filter.value })
      this.filter = filter
    },
    async getBookmarks() {
      const token = sessionStorage.getItem('_at')
      this.bookmarks = await getBookmarks(token)

      if (this.bookmarks.status === 401) {
        const refreshedToken = await getRefreshedTokens()

        if (refreshedToken.status === 401) return this.$router.push('/signin')
        else sessionStorage.setItem('_at', refreshedToken._at)

        this.bookmarks = await getBookmarks(refreshedToken._at)
      }
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/account/bookmarks";
</style>
