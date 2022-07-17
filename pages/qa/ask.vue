<template>
  <div class="ask-wrapper">
    <Input
      v-model="title"
      :title="'Question title'"
    />
    <client-only>
      <vue-editor class="VueEditor" />
    </client-only>
    <Button />
  </div>
</template>

<script>
import { getQuestionBySlug } from '~/api'
import Input from '~/components/basicComponents/Input'
import Button from '~/components/basicComponents/Button'
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
      content: null
    }
  },
  watch: {
    async title() {
      await this.getPostsBySlug()
    }
  },
  methods: {
    async getPostsBySlug() {
      if (this.title.length > 0)
        this.slugPosts = await getQuestionBySlug(this.title.split(' ').join('-').toLowerCase())
    },
    async postQuestion() {

    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa/ask";
</style>
