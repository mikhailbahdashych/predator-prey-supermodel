<template>
  <div class="ask-wrapper">

    <div class="ask-wrapper__elem">
      <Input
        v-model="title"
        :disabled="loading"
        :input-class="'small white-stroke'"
        :title="'Question title'"
      />
      <div v-if="showSimilarQuestions">
        <div v-for="sq in similarQuestions" :key="sq.slug">
          {{ sq }}
        </div>
      </div>
    </div>

    <div class="ask-wrapper__elem">
      <custom-vue-editor
        v-model="content"
      />
    </div>

    <div class="ask-wrapper__elem ask-wrapper__elem--button">
      <Button
        :disabled="loading"
        :label="'Ask question'"
        :btn-class="'min-width150'"
        @click-handler="postQuestion"
      />
    </div>

  </div>
</template>

<script>
import { createQuestionPost, getRefreshedTokens, getSimilarQuestions } from '~/api'
import Input from '~/components/basicComponents/Input'
import Button from '~/components/basicComponents/Button'
import CustomVueEditor from '~/components/basicComponents/CustomVueEditor'
import logout from '~/mixins/logout'
export default {
  name: 'Ask',
  components: {
    Input,
    Button,
    CustomVueEditor
  },
  mixins: [logout],
  layout: 'default',
  data() {
    return {
      similarQuestions: [],

      title: null,
      titleLength: null,
      content: null,

      showSimilarQuestions: false,
      loading: true
    }
  },
  watch: {
    title() {
      this.titleLength = this.title.split(' ')
    },
    'titleLength.length': async function () {
      await this.getPostsBySlug()
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    await this.checkToken()
  },
  methods: {
    async checkToken() {
      const refreshedToken = await getRefreshedTokens()

      if (refreshedToken.error?.errorMessage === 'invalid-token') return await this.logout()
      else sessionStorage.setItem('_at', refreshedToken._at)
    },
    async getPostsBySlug() {
      if (this.title.length > 0) {
        const slug = this.title
          .toLowerCase()
          .trim()
          .replace(/[^\w\s-]/g, '')
          .replace(/[\s_-]+/g, '-')
          .replace(/^-+|-+$/g, '');
        this.similarQuestions = await getSimilarQuestions(slug)
        this.showSimilarQuestions = true
      } else {
        this.showSimilarQuestions = false
      }
    },
    async postQuestion() {
      this.loading = true

      const data = await createQuestionPost({
        title: this.title,
        content: this.content,
      }, sessionStorage.getItem('_at'))

      if (data.message === 'success')
        return this.$router.push(`/qa/question/${data.slug}`)

      this.loading = false
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa";
</style>
