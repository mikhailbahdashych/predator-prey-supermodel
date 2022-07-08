<template>
  <div>
    <div class="account-preferences">
      <Input
        :title="'First name'"
      />
      <Input
        :title="'Last name'"
      />
      <Textarea
        :title="'About'"
      />
    </div>
  </div>
</template>

<script>
import Input from '~/components/Input';
import Textarea from "~/components/Textarea";
// import Button from "~/components/Button";
export default {
  name: 'PersonalInformation',
  components: {
    Input,
    Textarea
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
