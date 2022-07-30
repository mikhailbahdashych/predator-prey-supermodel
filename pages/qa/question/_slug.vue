<template>
  <div>
    <popup v-if="showPopup" :content="'Added to bookmarks'" />
    <div class="ask-wrapper">

      <div class="ask-wrapper__question-title">
        <div class="ask-wrapper__back-btn" @click="goBack">
          <img :src="require('../../../assets/img/backarrow.svg')" alt='Back' width='32' height='32'>
        </div>
        <skeleton v-if="loading" />
        <h1 v-else>{{ question.title }}</h1>
        <skeleton v-if="loading" />
        <div v-else class="ask-wrapper__title-box">
          <p class="ask-wrapper__preview-block">Views: {{ question.views }}</p>
          <p
            class="ask-wrapper__preview-block ask-wrapper__preview-block--answer"
            :class="question.is_answered ? 'ask-wrapper__preview-block--answered' : question.votes < 0 ? 'ask-wrapper__preview-block--low-quality-question' : ''"
          >Votes: {{ question.votes  }}</p>
        </div>
        <skeleton v-if="loading" />
        <div v-else class="ask-wrapper__info">
          <p class="opacity">Asked at: {{ question.created_at }}</p>
          <p class="opacity">Asked by: {{ question.username }}</p>
        </div>
      </div>

      <div class="ask-wrapper__question-title">
        <div class="ask-wrapper__content">
          <div class="ask-wrapper__votes">
            <p class="ask-wrapper__vote ask-wrapper__vote--up"
               @click="voteForQuestion('up')"
            >
              Upvote
            </p>
            <p class="ask-wrapper__vote ask-wrapper__vote--down"
               @click="voteForQuestion('down')"
            >
              Downvote
            </p>
            <p class="ask-wrapper__vote ask-wrapper__vote--bookmark"
               @click="addToBookmark"
            >
              Bookmark
            </p>
          </div>
          <div class="ask-wrapper__question-title--content">
            <p v-html="question.content" />
          </div>
        </div>
      </div>

      <div class="ask-wrapper__question-title ask-wrapper--no-border">
        <div v-if="!answers.length" class="ask-wrapper__no-answers">
          <p v-if="!showWantToAsk" class="source-sans-pro opacity">There are no answers for this question yet.</p>
          <p v-if="!showWantToAsk" class="source-sans-pro opacity">If you know the answer, go on and post it!</p>

          <div v-if="!showWantToAsk" class="ask-wrapper__no-answers ask-wrapper__no-answers--btn">
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
            <div class="ask-wrapper__no-answers ask-wrapper__no-answers--btn">
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
  </div>
</template>

<script>
import { getQuestion, answerQuestion, vote, createBookmark } from '~/api'
import { validateSlug } from '~/helpers/frontValidator'
import { verifyToken } from '~/helpers/crypto'
import Button from '~/components/basicComponents/Button'
import Popup from '~/components/basicComponents/Popup'
import Skeleton from '~/components/skeleton/Skeleton'
import CustomVueEditor from '~/components/basicComponents/CustomVueEditor'
export default {
  name: 'Slug',
  components: {
    CustomVueEditor,
    Skeleton,
    Button,
    Popup
  },
  layout: 'default',
  validate({ params }) { return validateSlug(params.slug) },
  data() {
    return {
      loading: true,
      status: null,
      question: {},
      answers: [],
      answer: null,
      isQuestionOwner: false,
      showWantToAsk: false,

      showPopup: false
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
    goBack() {
      this.$router.push('/qa')
    },
    showAnswerEditor() {
      this.showWantToAsk = true
    },
    async addToBookmark() {
      // @TODO Is there even sense to validate it on front end?
      const token = sessionStorage.getItem('_at')

      if (!token) {
        return this.$router.push('/signin')
      } else {
        const tokenData = verifyToken(token)
        if (tokenData.message === 'invalid-token')
          return this.$router.push('/signin')
      }

      const { message } = await createBookmark({
        type: 'question',
        id: this.question.id
      }, sessionStorage.getItem('_at'))
      if (message === 'success') {
        this.showPopup = true
        setTimeout(() => {
          this.showPopup = false
        }, 1500)
      }
    },
    async voteForQuestion(type) {
      const { status } = await vote({
        id: this.question.id, vote: type, type: 'question'
      }, sessionStorage.getItem('_at'))
      this.status = status
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
