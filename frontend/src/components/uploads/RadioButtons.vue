<template>
  <div class="radio-wrap">
    <h2 class="how-will-you">How will you upload files?</h2>
    <div class="button-wrap">
      <div class="single-radio">
        <h3>Copy/Paste URL</h3>
        <input
          type="radio"
          v-model="uploadType"
          value="1"
          @change="
            event => {
              $emit('uploadTypeSelection', event.target.value);
            }
          "
        />
      </div>
      <div class="single-radio">
        <h3>Upload File(s)</h3>
        <input
          type="radio"
          v-model="uploadType"
          value="2"
          @change="
            event => {
              $emit('uploadTypeSelection', event.target.value);
            }
          "
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploadType: null
    };
  },
  props: {
    uploadTypes: {
      type: null,
      required: true
    }
  }
};
</script>

<style>
.button-wrap {
  display: flex;
  margin: 0 auto;
  width: 75%;
  justify-content: space-around;
}
.how-will-you {
  padding: 10px 0;
}
.radio-wrap {
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.single-radio {
  width: 50%;
}
</style>
