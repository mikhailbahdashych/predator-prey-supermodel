<template>
  <div>
    <div class="account-preferences">

      <div class="profile-picture"></div>
      <div class="fields">
        <div class="flex">
          <Input
            v-model="personalInfo.first_name"
            :title="'First name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.last_name"
            :title="'Last name'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
        <Textarea
          v-model="personalInfo.about_me"
          :title="'About'"
        />
        <div class="flex">
          <Input
            v-model="personalInfo.website_link"
            :title="'Website'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.twitter"
            :title="'Twitter'"
            :title-class="'small'"
            :additional-class="'small'"
          />
          <Input
            v-model="personalInfo.github"
            :title="'GitHub'"
            :title-class="'small'"
            :additional-class="'small'"
          />
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import Input from '~/components/Input';
// import Textarea from "~/components/Textarea";
// import Button from "~/components/Button";
export default {
  name: 'PersonalInformation',
  components: {
    Input,
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
