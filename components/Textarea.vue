<template>
  <div>
    <p :class="`paragraph`">{{ title }}</p>
    <textarea
      ref="input"
      :value="value"
      class="bi textarea"
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
@import "../assets/css/components/Input";
</style>
