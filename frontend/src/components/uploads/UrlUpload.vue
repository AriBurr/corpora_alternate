<template>
  <div class="input-wrap">
    <input type="text" v-on:keydown.enter="$listeners" v-model="upload" />
  </div>
</template>

<script>
export default {};
</script>

<style></style>
