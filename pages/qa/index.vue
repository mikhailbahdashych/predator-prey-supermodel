<template>
  <div class="question-wrapper">

    <div class="question-wrapper__question-header">
      <h1>Q&A - Ask and answer</h1>
      <div class="question-wrapper__question-header-button">
        <Button
          :label="'Ask question'"
          :btn-class="'min-width150 transparent'"
          @click-handler="redirect('/qa/ask')"
        />
      </div>
    </div>

    <div class="question-wrapper__question-header-filter">
      <p
        v-for="item in sortTypes"
        :key="item.title"
        class="question-wrapper__sort-bar-item"
        :class="item.active ? 'question-wrapper__sort-bar-item--active' : ''"
      >
          <span
            :class="!item.active ? 'opacity' : ''"
            @click="sortBy(item)"
          >{{ item.title }}</span>
      </p>
    </div>

    <div class="question-wrapper__question-content">
      <div v-for="(q, i) in questions" :key="i" class="question-wrapper__question" @click="redirect(`/qa/question/${q.slug}`)">
        <div class="question-wrapper__title-box">
          <h3 class="question-wrapper__hover">{{ q.title }}</h3>
          <p class="opacity">Asked at: {{ q.created_at }}</p>
        </div>
        <div class="question-wrapper__title-box question-wrapper__title-box--no-baseline">
          <div class="question-wrapper__title-box">
            <p class="question-wrapper__preview-block">Views: {{ q.views }}</p>
            <p class="question-wrapper__preview-block">Answers: {{ q.count || 0 }}</p>
            <p
              class="question-wrapper__preview-block question-wrapper__preview-block--answer"
              :class="q.is_answered ? 'question-wrapper__preview-block--answered' : q.votes < 0 ? 'question-wrapper__preview-block--low-quality-question' : ''"
            >Votes: {{ q.votes  }}</p>
          </div>
          <div class="question-wrapper__title-box">
            <img class="question-wrapper__avatar-box" :src="require('../../assets/img/testava.jpg')" alt="ava">
          </div>
        </div>
      </div>
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
      sortTypes: [
        { title: 'Latest', active: true },
        { title: 'Hottest', active: false },
        { title: 'Week', active: false },
        { title: 'Month', active: false },
      ],
      sort: 'latest',
      questions: []
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.getQuestions()
  },
  methods: {
    async sortBy(item) {
      this.sortTypes.forEach(type => { type.active = type.title === item.title })
      this.sort = item.title
      await this.getQuestions()
    },
    async getQuestions() {
      this.questions = await getQuestions({
        sort: this.sort
      })
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
