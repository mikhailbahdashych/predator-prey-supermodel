<template>
  <div></div>
</template>

<script>
import {verifyClientByToken} from "~/helpers/auth";
export default {
  name: "Edit",
  async mounted() {
    await verifyClientByToken(this.$router, localStorage.getItem('token'))
  }
}
</script>

<style scoped>

</style>
