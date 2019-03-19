<template>
  <div class="input-wrap">
    <select
      v-model="selectedLanguage"
      @input="
        event => {
          $emit('languageSelection', event.target.value);
        }
      "
    >
      <option disabled>Select a Language</option>
      <option
        v-for="option in languages"
        :value="option.text"
        :key="option.value"
        >{{ option.text }}</option
      >
    </select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedLanguage: null
    };
  },
  props: {
    value: null,
    languages: {
      type: Array,
      required: true
    }
  },
  mounted() {
    this.selectedLanguage = this.value;
  },
  watch: {
    value: function(newValue) {
      this.selectedLanguage = newValue;
    }
  }
};
</script>

<style>
.input-wrap {
  width: 50%;
}
</style>
