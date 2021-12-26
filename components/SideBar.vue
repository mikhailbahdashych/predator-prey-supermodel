<template>
  <div class='side-bar'>
    <nuxt-link to="/" style="text-decoration: none; color: white; text-align: center;">
      <h1>pNb</h1>
    </nuxt-link>
    <div class='side-bar-menu'>
      <ul>
        <li @click='redirect("bmp")'><span class="underline-text"><a class='link-href'>Blog main page</a></span></li>
        <li><span class="underline-text"><a class='link-href'>Articles</a></span></li>
        <li><span class="underline-text"><a class='link-href'>Write-ups</a></span></li>
        <li><span class="underline-text"><a class='link-href'>Tips</a></span></li>
        <li><span class="underline-text"><a class='link-href'>CTF's</a></span></li>
      </ul>
      <div class='filters'>
        <p>Filter by dates:</p>
        <div v-click-outside='hideDatePicker'>
          <div @click='showDatePicker = !showDatePicker'>
            <input
              :class="{'date-pick-active' : showDatePicker}"
              class='date-pick'
              disabled :value='fullDate'
              @click='showDatePicker = !showDatePicker'
            >
          </div>
          <v-date-picker v-if='showDatePicker' v-model="range" is-dark is-range style='position: absolute' />
        </div>
        <button class="btn-hover color-5">FILTER</button>
      </div>
    </div>
  </div>
</template>

<script>
import moment from "moment";
import vClickOutside from 'v-click-outside';
export default {
  name: 'SideBar',
  components: {},
  directives: {
    clickOutside: vClickOutside.directive
  },
  data() {
    return {
      showDatePicker: false,
      range: {
        start: moment().subtract(6, 'days').format('YYYY-MM-DD'),
        end: moment().format('YYYY-MM-DD')
      },
    }
  },
  computed: {
    formattedDateStart() {
      return moment(this.range.start).format('YYYY-MM-DD')
    },
    formattedDateEnd() {
      return moment(this.range.end).format('YYYY-MM-DD')
    },
    fullDate() {
      const from = this.formattedDateStart
      const to = this.formattedDateEnd
      return from.toString() + " — " + to.toString()
    }
  },
  methods: {
    hideDatePicker() {
      this.showDatePicker = false
    },
    redirect(p) {
      switch (p) {
        case "bmp":
          this.$router.push({
            path: '/blog'
          })
          break
      }
    }
  }
}
</script>

<style lang='scss'>
@import "../assets/css/sidebar";
</style>
