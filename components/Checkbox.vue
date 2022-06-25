<template>
  <div class="checkbox-container">
    <label class="container">
      <input type="checkbox" :value="innerValue" :disabled="disabled" @input="onInput" >
      <span class="checkmark"></span>
    </label>
    <p class="checkbox-paragraph" v-html="label" />
  </div>
</template>

<script>
export default {
  name: "Checkbox",
  props: {
    label: {
      type: String,
      default: ''
    },
    value: {
      type: Boolean,
      default: false
    },
    disabled: {
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
    value(value) {
      this.innerValue = value
    },
    innerValue(value) {
      this.$emit('input', value)
    }
  },
  methods: {
    onInput() {
      this.$nextTick(() => {
        this.innerValue = !this.innerValue
      })
    }
  }
}
</script>

<style lang="scss">
@import "../assets/css/components/Checkbox";
</style>
