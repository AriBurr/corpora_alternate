<template>
  <div class="wrapper">
    <h1 class="uploads-header">Upload Files or URLs</h1>
    <div class="lang-select-wrap">
      <h1 class="lang-select-header">Select a language to upload:</h1>
      <LanguageSelect
        v-model="selectedLanguage"
        :languages="languages"
        @languageSelection="languageSelection"
      />
    </div>
    <RadioButtons
      v-model="uploadType"
      :uploadTypes="uploadTypes"
      @uploadTypeSelection="uploadTypeSelection"
    />
    <Uploader
      v-if="uploadType !== null"
      @determineUploadType="determineUploadType"
      v-model="uploadedItem"
    />
  </div>
</template>

<script>
import LanguageSelect from "../components/uploads/LanguageSelect";
import Uploader from "../components/uploads/Uploader";
import RadioButtons from "../components/uploads/RadioButtons";
import axios from "axios";

export default {
  components: { LanguageSelect, RadioButtons, Uploader },
  data() {
    return {
      uploadedItem: "",
      uploadType: null,
      uploadTypes: [{ name: "File", id: 1 }, { name: "URL", id: 2 }],
      selectedLanguage: false,
      languages: []
    };
  },
  mounted() {
    axios.get("/languages").then(r => (this.languages = r.data));
  },
  methods: {
    languageSelection(e) {
      this.selectedLanguage = e;
    },
    uploadTypeSelection(e) {
      this.uploadType = parseInt(e);
    },
    determineUploadType(item, title) {
      if (this.uploadType === 1) {
        alert("first one");
        return;
      } else if (this.uploadType === 2) {
        console.log("farts");
        console.log(item);
        console.log(title);
        axios.post("/upload_url/", { title, url: item });
        return;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.uploads-header {
  padding: 10px;
  font-size: 4em;
}
.lang-select-wrap {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
}
.lang-select-header {
  font-size: 2.5em;
}
</style>
