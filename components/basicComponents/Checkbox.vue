<template>
  <div class="checkbox-container">
    <label class="container">
      <input v-model="model" type="checkbox" :value="inputValue" :disabled="disabled" >
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
    inputValue: {
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
@import "../../assets/css/basicComponents/Checkbox";
</style>
