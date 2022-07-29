<template>
  <div class="confirmation">

  </div>
</template>

<script>
import { confirmAccount } from '~/api'
export default {
  name: 'Link',
  layout: 'empty',
  data() {
    return {

    }
  },
  async mounted() {
    await confirmAccount({
      activationLink: this.$route.params.link
    })
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/confirmation";
</style>
