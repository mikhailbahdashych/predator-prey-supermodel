<template>
  <div>

  </div>
</template>

<script>
import { getQuestionBySlug } from '~/api'
// import { validateSlug } from '~/helpers/frontValidator'
export default {
  name: 'Slug',
  layout: 'default',
  // validate({ params }) { return validateSlug(params.slug) },
  data() {
    return {
      loading: true,
      question: {}
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  async mounted() {
    this.question = await getQuestionBySlug(this.$route.params.slug)
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/qa/index";
</style>
