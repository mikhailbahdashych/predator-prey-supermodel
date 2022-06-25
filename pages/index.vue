<template>
  <div class='main'>
    <Header />
    <div class="content">
      <div class="center-text">
        <h1 class='big-text'>
          <span class="typed-text">{{ typeValueMain }}</span>
          <span class="cursor" :style="[showCursorMain ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusMain}">&nbsp;</span>
        </h1>
        <h1 class='big-text small'>
          <span class="typed-text">{{ typeValueSec }}</span>
          <span class="cursor" :style="[showCursorSec ? {'display' : 'inline-block'} : {'display' : 'none'}]" :class="{'typing': typeStatusSec}">&nbsp;</span>
        </h1>
      </div>
    </div>

    <div class="about">

      <LatestReleasesSkeleton v-if='loading' q='3' />

      <div class="right-about">

      </div>
    </div>

    <div class="about blog">
      <div class="left-about">

      </div>
      <div class="right-about">

      </div>
    </div>

    <Footer/>
  </div>
</template>

<script>
import moment from 'moment'
import Header from '~/components/Header';
import Footer from '~/components/Footer';
import LatestReleasesSkeleton from '~/components/Skeletons/LatestReleasesSkeleton';
import { typer } from '~/mixins/typer';
import { getLatestReleases } from '~/api'
export default {
  components: {
    Header,
    Footer,
    LatestReleasesSkeleton
  },
  mixins: [typer],
  data() {
    return {
      loading: true,
      latestReleases: [],
      test: null
    }
  },
  head() {
    return {
      bodyAttrs: {
        class: 'reset-body'
      }
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
    setTimeout(this.typeTextMain, this.newTextDelayMain + 200);
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
.reset-body {
  margin: 0;
}
</style>
