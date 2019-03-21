import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    primaryColor: "#6495ed"
  },
  mutations: {
    setThemeColor(state, color) {
      state.primaryColor = color;
    }
  },
  actions: {
    themeColor: state => state.primaryColor
  }
});
