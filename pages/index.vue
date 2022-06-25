<template>
  <div class='main'>
    <Header />
    <div class="content">
      <div class="center-text">
      </div>
    </div>

    <div class="about">
    </div>

    <div class="about blog">
    </div>

    <Footer/>
  </div>
</template>

<script>
import moment from 'moment'
import Header from '~/components/Header';
import Footer from '~/components/Footer';
import { getLatestReleases } from '~/api';
export default {
  components: {
    Header,
    Footer
  },
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
  mounted() {
    this.$nextTick(async () => {
      this.latestReleases = await getLatestReleases(3)
      Object.keys(this.latestReleases).forEach(x => {
        this.latestReleases[x].created_at = moment(this.latestReleases[x].created_at).format('YYYY-MM-DD HH:mm:ss')
      })
      this.loading = false
    })
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
