<template>
  <div class="ask-wrapper">

    <div class="mb">
      <Input
        v-model="title"
        :disabled="loading"
        :additional-class="'small white-stroke'"
        :title="'Question title'"
      />
      <div class="similar-questions">

      </div>
    </div>

    <client-only>
      <div class="editor">
        <vue-editor
          v-model="content"
        />
      </div>
    </client-only>

    <div class="editor">
      <Checkbox
        v-model="notify"
        :input-value="notify"
        :disabled="loading"
        :label="'Notify me, when the question is answered'"
      />
      <div class="ask-button">
        <Button
          :disabled="loading"
          :label="'Ask question'"
          :additional-class="'min-width150'"
          @click-handler="postQuestion"
        />
      </div>
    </div>

  </div>
</template>

<script>
import { getQuestionBySlug, createQuestionPost } from '~/api'
import Input from '~/components/basicComponents/Input'
import Button from '~/components/basicComponents/Button'
import Checkbox from '~/components/basicComponents/Checkbox'
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Ask',
  components: {
    VueEditor: async () => process.client ? (await import("vue2-editor")).VueEditor : "",
    Input,
    Button,
    Checkbox
  },
  layout: 'default',
  data() {
    return {
      similarQuestions: [],

      title: null,
      titleLength: null,
      content: null,
      notify: false,

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
        this.similarQuestions = await getQuestionBySlug(this.title.split(' ').join('+').toLowerCase())
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
        notify: this.notify
      }, sessionStorage.getItem('_at'))

      if (data.status === 1)
        return this.$router.push(`/qa/question/${data.questionId}`)

      this.loading = false
    }
  }
}
</script>

<style scoped>
.ask-wrapper {
  width: 45%;
  margin: 0 auto;
}
.similar-questions {
}
.ask-button {
  width: 150px;
}
.editor {
  padding: 0 5px 0 5px;
}
::v-deep .ql-toolbar.ql-snow {
  border-radius: 8px 8px 0 0;
  border: 1px solid rgba(225, 232, 236, .25);
  border-bottom: none;
}
::v-deep #quill-container {
  border-radius: 0 0 8px 8px;
  border: 1px solid rgba(225, 232, 236, .25);
}
</style>
