<template>
  <div class="question-wrapper asked-question">

    <div class="question-header">
      <h1>{{ question.title }}</h1>
    </div>

    <div>
      <p class="paragraph" v-html='question.content' />
    </div>

    <div>
      <p class="paragraph">{{ answers }}</p>
    </div>

    <h3>Your answer:</h3>
    <client-only>
      <div class="editor">
        <vue-editor v-model="answer" />
      </div>
    </client-only>

    <Button
      :label="'Post answer'"
      :additional-class="'min-width150 mt'"
      @click-handler="answerQuestion"
    />

  </div>
</template>

<script>
import { getQuestion, answerQuestion } from '~/api'
import { validateSlug } from '~/helpers/frontValidator'
import Button from '~/components/basicComponents/Button'
export default {
  name: 'Slug',
  components: {
    VueEditor: async () => process.client ? (await import("vue2-editor")).VueEditor : "",
    Button
  },
  layout: 'default',
  validate({ params }) { return validateSlug(params.slug) },
  data() {
    return {
      loading: true,
      question: {},
      answers: [],
      answer: null
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
    async answerQuestion() {
      await answerQuestion({
        question_id: this.question.id,
        answer_text: this.answer
      }, sessionStorage.getItem('_at'))
    }
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/qa/index";
</style>
