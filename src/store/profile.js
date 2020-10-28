import axios from '@/api/httpClient1';

const profile = {
  state: {
    favourites: [],
  },
  mutations: {
    'SET_FAVOURITES' (state, favourites) {
      state.favourites = favourites;
    }
  },
  actions: {
    setFavourites ({commit}) {
      let config = {
        headers: {
          "Content-Type": "application/json",
          "Authorization": "Bearer " + localStorage.getItem("access"),
          'Cache-Control': 'no-cache'
        }
      }
      axios.get('/api/accounts/favourites/ids/', config)
        .then(res => {
          commit('SET_FAVOURITES', res.data[0].channels)
        })
        .catch(error => {
          // console.log(error)
        })
    }
  },
  getters: {
    getFavourites (state) {
      return state.favourites;
    },
  }
};

export default profile
