import Vue from "vue"
import App from "./App.vue"
import router from "./router"
import store from "./store"
import Vuelidate from 'vuelidate'
import 'bootstrap-css-only/css/bootstrap.min.css'
import 'mdbvue/lib/css/mdb.min.css'
import '@fortawesome/fontawesome-free/css/all.min.css'
import InfiniteLoading from 'vue-infinite-loading'
import VueProgressBar from 'vue-progressbar'

const options = {
  color: 'rgb(143, 255, 199)',
  thickness: '2px',
  transition: {
    speed: '1.5s',
    opacity: '0.6s',
    termination: 400
  },
}

Vue.use(InfiniteLoading);
Vue.use(Vuelidate);
Vue.use(VueProgressBar, options)

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
