import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from 'vuelidate'
import 'bootstrap-css-only/css/bootstrap.min.css';
import 'mdbvue/lib/css/mdb.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import InfiniteLoading from 'vue-infinite-loading';
import axios from 'axios';

Vue.use(InfiniteLoading);
Vue.use(Vuelidate);

axios.defaults.baseURL = process.env.VUE_APP_BASEURL;
axios.defaults.headers.common['Authorization'] = process.env.VUE_APP_AUTHORIZATION;
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
