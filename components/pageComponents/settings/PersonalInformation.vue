<template>
  <div>
    <div class="account-preferences">

    </div>
  </div>
</template>

<script>
export default {
  name: 'PersonalInformation',
  props: {
    personalSettings: {
      type: Object,
      default: () => {}
    }
  },
  data() {
    return {
      personalInfo: {}
    }
  },
  mounted() {
    this.personalInfo = this.personalSettings
  },
  methods: {
  },
}
</script>

<style lang="scss">
@import "../../../assets/css/edit";
</style>
