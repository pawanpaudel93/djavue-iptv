import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    countries: null,
    categories: null,
  },
  mutations: {
    'SET_COUNTRIES' (state, countries) {
      state.countries = countries;
    },
    'SET_CATEGORIES' (state, categories) {
      state.categories = categories;
    }
  },
  actions: {
    setCountries ({commit}) {
      axios.get('/api/iptv/titles/country/')
        .then(res => {
          commit('SET_COUNTRIES', res.data.country)
        })
        .catch(error => {
          console.log(error)
        })
    },
    setCategories ({commit}) {
      axios.get('/api/iptv/titles/category/')
        .then(res => {
          commit('SET_CATEGORIES', res.data.category)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  getters: {
    getCountries (state) {
      return state.countries;
    },
    getCategories (state) {
      return state.categories;
    }
  }
});
