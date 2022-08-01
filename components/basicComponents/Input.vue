<template>
  <div :class="onWhite ? `basic-input-container basic-input-container--color-on-white` : `basic-input-container`">
    <p class="small">{{ title }}</p>
    <input
      ref="name"
      class="bi bi--basic-input"
      :class="[
        (onError && innerValue && innerValue.length > 0 ?
         `bi--basic-input__error ${inputClass}` : readonly ? `bi--basic-input__readonly ${inputClass}` :
          inputClass)]"
      :type="type"
      :disabled="disabled"
      :readonly="readonly"
      :placeholder="placeholder"
      :name="name"
      :value="innerValue"
      @input="onInput"
    >
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    title: {
      type: String,
      default: ''
    },
    value: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'text'
    },
    name: {
      type: String,
      default: ''
    },
    disabled: {
      type: Boolean,
      default: false
    },
    readonly: {
      type: Boolean,
      default: false
    },
    placeholder: {
      type: String,
      default: ''
    },
    inputClass: {
      type: String,
      default: ''
    },
    focus: {
      type: Boolean,
      default: false
    },
    onError: {
      type: Boolean,
      default: false
    },
    onWhite: {
      type: Boolean,
      default: false
    }
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
@import "../../assets/css/basicComponents/Input";
</style>
