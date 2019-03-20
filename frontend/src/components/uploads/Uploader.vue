<template>
  <div class="uploader-wrap">
    <input
      class="uploadInput"
      placeholder="Title"
      v-model="uploadedTitle"
      type="text"
    />
    <input
      class="uploadInput"
      placeholder="URL"
      v-model="uploadedItem"
      type="text"
    />
    <div
      class="submitButton"
      @click="
        event => {
          $emit('handleURLUpload', uploadedItem, uploadedTitle);
        }
      "
    >
      <h1>Submit</h1>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uploadedItem: null,
      uploadedTitle: null
    };
  }
};
</script>

<style>
.uploadInput {
  width: 75%;
  text-align: center;
  margin-top: 20px;
  padding: 0 50px;
  font-size: 16px;
  height: 50px;
  border-radius: 10px;
  border: 2px solid gainsboro;
  box-shadow: 0 0 15px 5px gainsboro;
}
.submitButton {
  width: 300px;
  border-radius: 10px;
  margin: 0 auto;
  margin-top: 30px;
  border: 2px solid pink;
  border: 2px solid gainsboro;
  box-shadow: 0 0 1px 1px gainsboro;
}
.submitButton:hover {
  cursor: pointer;
  box-shadow: 0px 0px 10px 5px gainsboro;
}
</style>
