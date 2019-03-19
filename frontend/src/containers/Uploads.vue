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
  </div>
</template>

<script>
// import FileUpload from "../components/uploads/FileUpload";
// import UrlUpload from "../components/uploads/UrlUpload";
import LanguageSelect from "../components/uploads/LanguageSelect";

export default {
  components: { LanguageSelect },
  data() {
    return {
      urlUpload: false,
      fileUpload: false,
      selectedLanguage: false,
      languages: [{ text: "english", value: 1 }, { text: "spansih", value: 2 }]
    };
  },
  // mounted(){
  //   axios.get('https:localhost:8000/languages')
  // },
  methods: {
    languageSelection(e) {
      this.selectedLanguage = e;
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
