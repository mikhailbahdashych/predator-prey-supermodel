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

    <div class="ask-wrapper__question-title">
      <div v-if="!answers.length" class="ask-wrapper__question-title__no-answers">
        <p v-if="!showWantToAsk" class="source-sans-pro opacity">There are no answers for this question yet.</p>
        <p v-if="!showWantToAsk" class="source-sans-pro opacity">If you know the answer, go on and post it!</p>

        <div v-if="!showWantToAsk" class="ask-wrapper__question-title__no-answers ask-wrapper__question-title__no-answers--btn">
          <Button
            :label="isQuestionOwner ? 'Yes, I know the answer for my own question' : 'Yes, I know the answer'"
            :btn-class="`basic-button--transparent`"
            @click-handler="showAnswerEditor"
          />
        </div>

        <div v-if="showWantToAsk">
          <custom-vue-editor
            v-model="answer"
          />
          <div class="ask-wrapper__question-title__no-answers ask-wrapper__question-title__no-answers--btn">
            <Button
              :label="'Post answer'"
              :btn-class="`basic-button--transparent`"
              @click-handler="answerQuestion"
            />
          </div>
        </div>

      </div>

      <div v-else></div>
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
      isQuestionOwner: false,
      showWantToAsk: false
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
    showAnswerEditor() {
      this.showWantToAsk = true
    },
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
