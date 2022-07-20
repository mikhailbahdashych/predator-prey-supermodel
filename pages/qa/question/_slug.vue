<template>
  <div class="question-wrapper asked-question">

    <div class="question-header">
      <h1>{{ question.title }}</h1>
    </div>

    <div>
      <p class="paragraph" v-html='question.content' />
    </div>
  </div>
</template>

<script>
import { getQuestion } from '~/api'
import { validateSlug } from '~/helpers/frontValidator'
export default {
  name: 'Slug',
  layout: 'default',
  validate({ params }) { return validateSlug(params.slug) },
  data() {
    return {
      loading: true,
      question: {},
      answers: []
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    const { question, answers } = await getQuestion(this.$route.params.slug)
    this.question = question
    this.answers = answers
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/qa/index";
</style>
