<template>
  <div class='side-bar'>
    <div v-if='loading'>
      <p class='skeleton-text skeleton-header'></p>
    </div>
    <div v-if='!loading'>
      <nuxt-link to="/" class='nuxt-link'>
        <h1 class='big-text blog-logo'>pNb</h1>
      </nuxt-link>
    </div>
    <div class='side-bar-menu'>
      <div v-if='loading'>
        <ul v-for='s in subpages.length' :key='s.value'>
          <li class='skeleton-text'></li>
        </ul>
      </div>
      <div v-if='!loading'>
        <ul v-for='sub in subpages' :key='sub.value'>
          <li @click='redirect(sub.value)'>
          <span class='underline-text'>
            <a class='link-href'>{{sub.name}}</a>
          </span>
          </li>
        </ul>
      </div>
      <div class='filters'>
        <p v-if='loading' class='skeleton-text plot'></p>
        <p v-if='!loading'>Filter by dates:</p>
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
            <div v-if='showFilter'
            style='width: 100px; height: 100px; position: absolute; background-color: greenyellow'>TEST</div>
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
      filters: ['A-Z', 'Z-A', 'Newest', 'Oldest', 'Most popular'],
      loading: true
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
  created() {
    this.$nextTick(() => {
      this.loading = false
    })
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
@import "../assets/css/main";
</style>
