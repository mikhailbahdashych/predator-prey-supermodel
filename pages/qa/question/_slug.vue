<template>
  <div class="ask-wrapper">

    <div class="ask-wrapper__question-title">
      <h1>{{ question.title }}</h1>
      <div class="ask-wrapper__question-title__title-box">
        <p class="ask-wrapper__question-title__preview-block">Views: {{ question.views }}</p>
        <p
          class="ask-wrapper__question-title__preview-block ask-wrapper__question-title__preview-block--answer"
          :class="question.is_answered ? 'ask-wrapper__question-title__preview-block--answered' : question.votes < 0 ? 'ask-wrapper__question-title__preview-block--low-quality-question' : ''"
        >Votes: {{ question.votes  }}</p>
      </div>
      <div class="ask-wrapper__question-title__info">
        <p class="opacity">Asked at: {{ question.created_at }}</p>
        <p class="opacity">Asked by: {{ question.username }}</p>
      </div>
    </div>

    <div class="ask-wrapper__question-title">
      <div class="ask-wrapper__question-title__content">
        <div class="ask-wrapper__question-title__content__votes"></div>
        <p v-html="question.content" />
      </div>
    </div>

    <h3>Post your answer:</h3>
    <custom-vue-editor
      v-model="answer"
    />

    <div class="ask-wrapper__elem ask-wrapper__elem--button">
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
