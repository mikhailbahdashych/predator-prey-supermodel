<template>
  <div class="ask-wrapper">

    <div class="elem">
      <Input
        v-model="title"
        :disabled="loading"
        :additional-class="'small white-stroke'"
        :title="'Question title'"
      />
    </div>

    <div class="elem">
      <custom-vue-editor
        v-model="content"
      />
    </div>

    <div class="elem button">
      <Button
        :disabled="loading"
        :label="'Ask question'"
        :additional-class="'min-width150'"
        @click-handler="postQuestion"
      />
    </div>

  </div>
</template>

<script>
import { getQuestion, createQuestionPost } from '~/api'
import Input from '~/components/basicComponents/Input'
import Button from '~/components/basicComponents/Button'
import CustomVueEditor from '~/components/basicComponents/CustomVueEditor'
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Ask',
  components: {
    Input,
    Button,
    CustomVueEditor
  },
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
  mounted() {
    this.decodeToken()
  },
  methods: {
    decodeToken() {
      const token = sessionStorage.getItem('_at')

      if (!token)
        return this.$router.push('/signin')

      const tokenData = verifyToken(token)

      if (tokenData.message === 'invalid-token')
        return this.$router.push('/signin')
    },
    async getPostsBySlug() {
      if (this.title.length > 0) {
        this.similarQuestions = await getQuestion(this.title.split(' ').join('+').toLowerCase())
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

      if (data.status === 1)
        return this.$router.push(`/qa/question/${data.slug}`)

      this.loading = false
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa";
</style>
