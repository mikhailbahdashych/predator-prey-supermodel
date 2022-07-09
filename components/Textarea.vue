<template>
  <div class="basic-textarea-outer">
    <p :class="`paragraph`">{{ title }}</p>
    <textarea
      ref="name"
      class="bi textarea"
      :value="innerValue"
      @input="onInput"
    />
  </div>
</template>

<script>
export default {
  name: "Textarea",
  props: {
    title: {
      type: String,
      default: ''
    },
  },
  data() {
    return {
      innerValue: this.value
    }
  },
  watch: {
    focus: function() {
      if (this.focus) this.$refs.name.focus()
    },
    value(value) {
      this.innerValue = value
    },
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

<style lang="scss">
@import "../assets/css/components/Input";
</style>
