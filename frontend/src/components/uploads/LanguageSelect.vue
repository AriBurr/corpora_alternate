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
        class="single-option"
        v-for="option in languages"
        :value="option.name"
        :key="option.value"
        >{{ option.name }}</option
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
select {
  width: 50%;
  padding: 5px;
  line-height: 1;
  font-size: 20px;
  text-align: center;
  border: 0;
  border-radius: 5px;
  height: 34px;
  background: url(http://cdn1.iconfinder.com/data/icons/cc_mono_icon_set/blacks/16x16/br_down.png)
    no-repeat right #ddd;
  -webkit-appearance: none;
  background-position-x: 95%;
}
.single-option {
  font-size: 16px;
}
</style>
