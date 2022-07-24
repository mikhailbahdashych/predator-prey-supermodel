<template>
  <div>
    <client-only>
      <div class="editor">
        <vue-editor
          v-model="innerValue"
        />
      </div>
    </client-only>
  </div>
</template>

<script>
export default {
  name: 'CustomVueEditor',
  components: {
    VueEditor: async () => process.client ? (await import("vue2-editor")).VueEditor : "",
  },
  props: {
    content: {
      type: String,
      default: ''
    },
  },
  data() {
    return {
      innerValue: this.content,
    }
  },
  watch: {
    innerValue(value) {
      this.$emit('input', value)
    }
  },
  methods: {
    onInput(event) {
      this.$nextTick(() => {
        this.innerValue = event.target.value
      })
    }
  }
}
</script>

<style scoped>
.editor {
  padding: 0 5px 0 5px;
}
::v-deep .ql-toolbar.ql-snow {
  border-radius: 8px 8px 0 0;
  border: 1px solid rgba(225, 232, 236, .25);
  border-bottom: none;
}
::v-deep .ql-toolbar.ql-snow:focus {
  border: 1px solid rgba(88, 167, 254, .25);
}
::v-deep #quill-container {
  border-radius: 0 0 8px 8px;
  border: 1px solid rgba(225, 232, 236, .25);
}
::v-deep #quill-container:focus {
  border: 1px solid rgba(88, 167, 254, .25);
}
</style>
