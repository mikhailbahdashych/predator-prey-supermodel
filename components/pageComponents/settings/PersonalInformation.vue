<template>
  <div>
    <div class="account-preferences">
      <div class="profile-picture"></div>
      <div class="fields"></div>
      <div class="flex">
        <Input
          :title="'First name'"
        />
        <Input
          :title="'Last name'"
        />
      </div>
      <Textarea
        :title="'About'"
      />
      <div class="flex">
        <Input
          :title="'Website'"
        />
        <Input
          :title="'Twitter'"
        />
        <Input
          :title="'GitHub'"
        />
      </div>

    </div>
  </div>
</template>

<script>
// import Input from '~/components/Input';
// import Textarea from "~/components/Textarea";
// import Button from "~/components/Button";
export default {
  name: 'PersonalInformation',
  components: {
    // Input,
    // Textarea
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
