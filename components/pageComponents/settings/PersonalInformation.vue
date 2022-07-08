<template>
  <div>
    <div class="account-preferences">
      <Input
        :title="'First name'"
      />
      <Input
        :title="'Last name'"
      />
    </div>
  </div>
</template>

<script>
import Input from '~/components/Input';
// import Button from "~/components/Button";
export default {
  name: 'PersonalInformation',
  components: {
    Input,
    // Button
  },
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
