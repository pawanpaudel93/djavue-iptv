import Vue from "vue";
import Vuex from "vuex";
import auth from './auth';
import profile from './profile';
import tv from './tv';
import VuexPersistence from 'vuex-persist'

const vuexLocal = new VuexPersistence({
  key: "rowdy",
  storage: window.localStorage,
  modules: ['auth',]
})

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    tv,
    auth,
    profile,
  },
  plugins: [vuexLocal.plugin]
});
