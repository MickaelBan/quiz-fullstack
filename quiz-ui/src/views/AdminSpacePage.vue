<template>
  <div class="list">
    <div class="button">
      <input type="submit" value="list of questions" v-on:click="$router.push({ name: 'DataList' })">
    </div>
    <div class="button">
      <input type="submit" value="Display questions" v-on:click="$router.push({ name: 'adminDisplay' })">
    </div>
  </div>
</template>

<script>

</script>