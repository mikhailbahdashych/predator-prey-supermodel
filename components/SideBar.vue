<template>
  <div class='side-bar'>
    <nuxt-link to="/" class='nuxt-link'>
      <h1 class='big-text blog-logo'>pNb</h1>
    </nuxt-link>
    <div class='side-bar-menu'>
      <ul v-for='sub in subpages' :key='sub.value'>
        <li @click='redirect(sub.value)'><span class='underline-text'>
          <a class='link-href'>{{sub.name}}</a>
        </span></li>
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
        <div>
          <div v-click-outside='hideFilters'>
            <div @click='showFilter = !showFilter'>
              <input disabled :class="{'date-pick-active' : showFilter}" class='date-pick' :value='filters[0]' @click='showFilter = !showFilter'>
            </div>
            <div style='width: 100px; height: 100px; position: absolute; background-color: greenyellow'
            v-if='showFilter'>TEST</div>
          </div>
        </div>
        <button class="ripple" @click='onClickButton'>FILTER</button>
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
  props: { 'subpages': {type: Array, required: true} },
  data() {
    return {
      showDatePicker: false,
      showFilter: false,
      range: {
        start: moment().subtract(6, 'days').format('YYYY-MM-DD'),
        end: moment().format('YYYY-MM-DD')
      },
      filters: ['A-Z', 'Z-A', 'Newest', 'Oldest', 'Most popular']
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
    onClickButton () {
      this.$emit('clicked', [this.formattedDateStart, this.formattedDateEnd])
    },
    hideDatePicker() {
      this.showDatePicker = false
    },
    hideFilters() {
      this.showFilter = false
    },
    redirect(p) {
      this.subpages.forEach(item => {
        if (item.value === p) {
          this.$router.push({
            path: item.page
          })
        }
      })
    }
  }
}
</script>

<style lang='scss'>
@import "../assets/css/sidebar";
</style>
