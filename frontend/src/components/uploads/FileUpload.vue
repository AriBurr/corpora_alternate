<template>
  <div id="app">
    <div class="file-select-wrap">
      <label>
        File
        <input
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
          multiple
        />
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      file: []
    };
  },
  methods: {
    submitFile() {
      for (var i = 0; i < this.file.length; i++) {
        let formData = new FormData();
        formData.append("file", this.file[i].file);
        formData.append("title", this.file[i].name);
        // formData.append("file_type", this.file[i].file_type);
        axios
          .post("/upload_file/", formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(function() {
            console.log("SUCCESS!!");
          })
          .catch(function() {
            console.log("FAILURE!!");
          });
      }
      return;
    },
    handleFileUpload() {
      for (var i = 0; i < this.$refs.file.files.length; i++) {
        this.file.push({
          file: this.$refs.file.files[i],
          title: this.$refs.file.files[i].name,
          file_type: this.$refs.file.files[i].type
        });
      }
    }
  }
  //   removeFile(key) {
  //     this.files.splice(key, 1);
  //   }
  // }
};
</script>

<style></style>
