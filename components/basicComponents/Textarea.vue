<template>
  <div class="basic-input-container">
    <p class="small">{{ title }}</p>
    <textarea
      ref="input"
      :value="value"
      class="bi bi--textarea"
      @input="updateValue($event.target.value)"
    ></textarea>
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
    value: {
      type: String,
      default: ''
    }
  },
  methods: {
    updateValue(value) {
      this.$refs.input.value = value;
      this.$emit('input', value);
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/Input";
</style>
