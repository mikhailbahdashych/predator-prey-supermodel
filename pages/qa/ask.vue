<template>
  <div class="ask-wrapper">
    <Input
      v-model="title"
      :title="'Question title'"
    />
    <client-only>
      <vue-editor v-model="content" class="VueEditor" />
    </client-only>
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
import { verifyToken } from '~/helpers/crypto'
export default {
  name: 'Ask',
  components: {
    VueEditor: async () => process.client ? (await import("vue2-editor")).VueEditor : "",
    Input,
    Button
  },
  layout: 'default',
  data() {
    return {
      slugPosts: [],
      title: null,
      content: null,
      notify: false
    }
  },
  watch: {
    async title() {
      await this.getPostsBySlug()
    }
  },
  mounted() {
    if (!sessionStorage.getItem('_at')) return this.$router.push('/')
    else return this.decodeToken()
  },
  methods: {
    decodeToken() {
      const token = sessionStorage.getItem('_at')
      const result = verifyToken(token)
      if (result.message === 'invalid-token') return this.$router.push('/')
    },
    async getPostsBySlug() {
      if (this.title.length > 0)
        this.slugPosts = await getQuestionBySlug(this.title.split(' ').join('-').toLowerCase())
    },
    async postQuestion() {
      const { status } = await createQuestionPost({
        title: this.title,
        content: this.content,
        notify: this.notify
      }, sessionStorage.getItem('_at'))
      // if (status === 1)
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa/ask";
</style>
