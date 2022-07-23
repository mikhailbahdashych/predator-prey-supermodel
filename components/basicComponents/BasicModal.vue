<template>
  <div class="settings-modal-container">
    <div class="settings-modal-container__settings-modal-wrapper">
      <div class="settings-modal-container__settings-modal-wrapper__modal-header">
        <img src='../../assets/img/backarrow.svg' alt="Back" @click="$emit('close')">
        <h3>{{header}}</h3>
      </div>
      <p class="settings-modal-container__settings-modal-wrapper__modal-description">{{description}}</p>
      <div class="settings-modal-container__settings-modal-wrapper">
        <slot/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BasicModal",
  props: {
    header: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="scss">
@import "../../assets/css/basicComponents/BasicModal";
</style>
