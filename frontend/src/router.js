import Vue from "vue";
import Router from "vue-router";
import Home from "./containers/Home.vue";
import Uploads from "./containers/Uploads";
import Recommender from "./containers/Recommender";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/uploads",
      name: "Uploads",
      component: Uploads
    },
    {
      path: "/recommender",
      name: "Recommender",
      component: Recommender
    }
  ]
});
