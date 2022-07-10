<template>
  <div class="checkbox-container">
    <label class="container">
      <input type="checkbox" :value="inputValue" :disabled="disabled" v-model="model" >
      <span class="checkmark"></span>
    </label>
    <p class="checkbox-paragraph" v-html="label" />
  </div>
</template>

<script>
export default {
  name: "Checkbox",
  props: {
    label: String,
    value: Boolean,
    inputValue: Boolean,
    disabled: Boolean
  },
  data() {
    return {
      innerValue: this.value
    }
  },
  computed: {
    model: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  }
}
</script>

<style lang="scss">
@import "../assets/css/components/Checkbox";
</style>
