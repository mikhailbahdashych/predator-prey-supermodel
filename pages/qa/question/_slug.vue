<template>
  <div class="ask-wrapper">

    <div class="question-title">
      <h1>{{ question.title }}</h1>
    </div>

    <div class="question-title">
      <p class="paragraph" v-html="question.content" />
    </div>

    <h3>Post your answer:</h3>
    <custom-vue-editor
      v-model="answer"
    />

    <div class="elem button">
      <Button
        :label="isQuestionOwner ? 'Yes, I want to answer my own question' : 'Yes, I want to answer'"
        :btn-class="'min-width150'"
        @click-handler="answerQuestion"
      />
    </div>

  </div>
</template>

<script>
import { getQuestion, answerQuestion } from '~/api'
import { validateSlug } from '~/helpers/frontValidator'
import { verifyToken } from '~/helpers/crypto'
import Button from '~/components/basicComponents/Button'
import CustomVueEditor from '~/components/basicComponents/CustomVueEditor'
export default {
  name: 'Slug',
  components: {
    CustomVueEditor,
    Button
  },
  layout: 'default',
  validate({ params }) { return validateSlug(params.slug) },
  data() {
    return {
      loading: true,
      question: {},
      answers: [],
      answer: null,
      wantToAsk: false,
      showWantToAsk: false,
      isQuestionOwner: false
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    const { question, answers } = await getQuestion(this.$route.params.slug)
    this.question = question
    this.answers = answers

    this.isQuestionOwner = verifyToken(sessionStorage.getItem('_at')).username === question.username
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
@import "../../../assets/css/pages/qa";
</style>
