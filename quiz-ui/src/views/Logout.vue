<template>

</template>

<script>
import AdminStorageService from '../services/AdminStorageService';
export default {
  created() {
    AdminStorageService.clear()
    this.$router.push({ name: "home" })
  }
}

</script>