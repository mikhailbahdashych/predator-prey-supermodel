<template>
  <div>
    <client-only>
      <vue-editor v-model="title" class="VueEditor" />
    </client-only>
  </div>
</template>

<script>
import { VueEditor } from "vue2-editor";
export default {
  name: 'Ask',
  components: {
    VueEditor
  },
  layout: 'default',
  data() {
    return {
      title: null
    }
  },
  methods: {

  }
}
</script>

<style lang="scss">
@import "../../assets/css/pages/qa/ask";
</style>
