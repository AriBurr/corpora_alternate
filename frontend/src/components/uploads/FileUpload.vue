<template>
  <div class="wrap">
    <div class="button-wrap">
      <div class="add-file btn" v-on:click="addFiles()">Add Files</div>
      <div class="file-select-wrap">
        <input
          class="inputFile"
          type="file"
          id="file"
          ref="file"
          v-on:change="handleFileUpload()"
          multiple
        />
        <button class="submit btn" v-on:click="submitFile()">Upload</button>
      </div>
    </div>
    <div v-if="file.length > 0" class="list-wrap">
      <h3 style="padding: 0 60px">File Name</h3>
      <div v-for="(s, key) in file" class="single-file" :key="key">
        {{ s.title }}
        <span class="remove-file" v-on:click="removeFile(key)">Remove</span>
      </div>
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
  props: ["selectedLanguage"],
  methods: {
    addFiles() {
      this.$refs.file.click();
    },
    submitFile() {
      for (var i = 0; i < this.file.length; i++) {
        let formData = new FormData();
        formData.append("file", this.file[i].file);
        formData.append("title", this.file[i].title);
        formData.append("file_type", this.file[i].file_type);
        formData.append("language_id", this.selectedLanguage);
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
    },
    removeFile(key) {
      this.file.splice(key, 1);
    }
  }
};
</script>

<style scoped>
.wrap {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  flex-direction: column;
}
.button-wrap {
  display: flex;
  width: 50%;
  justify-content: space-around;
  align-items: center;
}
.list-wrap {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 75%;
}
.single-file {
  display: flex;
  height: 50px;
  width: 90%;
  align-items: center;
  justify-content: space-between;
  margin: 2px auto;
  border: 2px solid #c6c8c7;
  padding: 0 20px;
}

.file-select-wrap {
  margin: 20px 0;
}
.submit {
  background-color: #332d8c;

  color: white;
}

.btn {
  border-radius: 10px;
  height: 60px;
  width: 150px;
  display: flex;
  align-items: center;
  font-size: 20px;
  justify-content: center;
}

.btn:hover {
  cursor: pointer;
  box-shadow: 0px 0px 3px 3px gray;
}
.inputFile {
  width: 0.1px;
  height: 0.1px;
  opacity: 0;
  overflow: hidden;
  position: absolute;
  top: -500px;
  z-index: -1;
}

.add-file {
  background-color: #fcd50b;

  color: black;
}

.remove-file {
  width: 20%;
  background-color: lightskyblue;
  height: 75%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px;
}
</style>
