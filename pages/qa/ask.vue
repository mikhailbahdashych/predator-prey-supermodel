<template>
  <div class="ask-wrapper">

    <Input
      v-model="title"
      :title="'Question title'"
    />

    <client-only>
      <vue-editor v-model="content" class="VueEditor" />
    </client-only>

    <Checkbox
      v-model="notify"
      :input-value="notify"
      :disabled="loading"
      :label="'Notify me, when someone answers'"
    />

    <Button
      :label="'Ask question'"
      @click-handler="postQuestion"
    />

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
      slugPosts: [],
      title: null,
      content: null,
      notify: false,
      loading: true
    }
  },
  watch: {
    async title() {
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
        return this.$router.push('/')

      const tokenData = verifyToken(token)

      if (tokenData.message === 'invalid-token')
        return this.$router.push('/')
    },
    async getPostsBySlug() {
      if (this.title.length > 0)
        this.slugPosts = await getQuestionBySlug(this.title.split(' ').join('+').toLowerCase())
    },
    async postQuestion() {
      const data = await createQuestionPost({
        title: this.title,
        content: this.content,
        notify: this.notify
      }, sessionStorage.getItem('_at'))
      if (data.status === 1)
        return this.$router.push(`/qa/question/${data.questionId}`)
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa/ask";
</style>
