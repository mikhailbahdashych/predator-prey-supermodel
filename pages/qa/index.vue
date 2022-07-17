<template>
  <div class="question-wrapper">

    <div class="question-header">
      <h1>Q&A - Ask and answer</h1>
      <div class="question-header-button">
        <Button
          :label="'Ask question'"
          :additional-class="'min-width150 transparent'"
          @click-handler="redirect('/qa/ask')"
        />
      </div>
    </div>

    <div class="question-content sort">
      <Button
        :label="'Latest'"
        :additional-class="`${sortType.latest ? 'mrl rounded': 'mrl rounded transparent'}`"
        @click-handler="sortBy('latest')"
      />
      <Button
        :label="'Hottest'"
        :additional-class="`${sortType.hottest ? 'mrl rounded': 'mrl rounded transparent'}`"
        @click-handler="sortBy('hottest')"
      />
      <Button
        :label="'Top week'"
        :additional-class="`${sortType.week ? 'mrl rounded': 'mrl rounded transparent'}`"
        @click-handler="sortBy('topOfTheWeek')"
      />
      <Button
        :label="'Top month'"
        :additional-class="`${sortType.month ? 'mrl rounded': 'mrl rounded transparent'}`"
        @click-handler="sortBy('topOfTheMonth')"
      />
    </div>

    <div class="question-content">

    </div>
  </div>
</template>

<script>
import Button from '~/components/basicComponents/Button'
import { getQuestions } from '~/api'
export default {
  name: 'Index',
  components: {
    Button
  },
  layout: 'default',
  data() {
    return {
      loading: true,
      sortType: {
        latest: true,
        hottest: false,
        week: false,
        month: false
      },
      sort: 'latest',
      question: []
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.getQuestions()
  },
  methods: {
    async sortBy(type) {
      Object.entries(this.sortType).forEach(item => { this.sortType[item[0]] = item[0] === type })
      this.sort = type
      await this.getQuestions()
    },
    async getQuestions() {
      this.question = await getQuestions(this.sort)
    },
    redirect(path) {
      this.$router.push(path)
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa";
</style>
