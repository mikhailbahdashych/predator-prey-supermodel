<template>
  <div>

  </div>
</template>

<script>
import { validateSlug } from '~/helpers/frontValidator'
export default {
  name: 'Slug',
  components: {
  },
  validate({ params }) { return validateSlug(parseInt(params.slug)) },
  data() {
    return {
      loading: true
    }
  },
  created() {
    this.$nextTick(() => { this.loading = false })
  },
  methods: {
  }
}
</script>

<style lang="scss">
@import "../../../assets/css/pages/blog";
</style>
