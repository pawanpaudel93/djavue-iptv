
import axios from '@/api/httpClient1';
import jwt_decode from 'jwt-decode';
import router from '@/router/index'

const auth = {
  state: {
    authUser: localStorage.getItem('user'),
    isAuthenticated: localStorage.getItem('isAuthenticated'),
    token: {
        access: localStorage.getItem('access'),
        refresh: localStorage.getItem('refresh')
    },
    endpoints: {
      obtainJWT: "/auth/jwt/create/",
      refreshJWT: "/auth/jwt/refresh/"
    },
    errorStatus: ''
  },
  mutations: {
    'SET_AUTHUSER' (state, status) {
      state.authUser = status.username;
      state.isAuthenticated = status.isAuthenticated;
      localStorage.setItem('user', status.username);
      localStorage.setItem('isAuthenticated', status.isAuthenticated);
    },
    'UPDATE_ACCESS' (state, access) {
        localStorage.setItem('access', access);
        state.token.access = access;
    },
    'UPDATE_TOKEN' (state, token) {
        localStorage.setItem('access', token.access);
        localStorage.setItem('refresh', token.refresh);
        state.token.access = token.access;
        state.token.refresh = token.refresh;
    },
    'LOGOUT' (state) {
        localStorage.removeItem('access');
        localStorage.removeItem('refresh');
        localStorage.removeItem('user');
        localStorage.removeItem('isAuthenticated');
        state.token.access = state.token.refresh = state.authUser = state.isAuthenticated = null;
        state.errorStatus = '';
    }
  },
  actions: {
    obtainToken({state, commit}, payload) {
      console.log(payload);
        axios.post(state.endpoints.obtainJWT, payload)
            .then(response => {
                console.log(response);
                state.errorStatus = '';
                commit('UPDATE_TOKEN', response.data);
                commit('SET_AUTHUSER', {
                  username: payload.username,
                  isAuthenticated: true
                })
                router.push("/");
            })
            .catch(error => {
                console.log(error.response)
                state.errorStatus = error.response.data.detail;
            })
    },
    refreshToken({state, commit}) {
        const payload = {
            refresh: state.token.refresh
        }
        axios.post(state.endpoints.refreshJWT, payload)
            .then(response => {
                commit('UPDATE_ACCESS', response.data.access)
            })
            .catch(error => {
                console.log(error.response.data)
            })
    },
    inspectToken ({state, dispatch, commit}) {
      const accessToken = state.token.access;
      const refreshToken = state.token.refresh;
      if (accessToken) {
        const decoded = jwt_decode(accessToken);
        const exp = decoded.exp;
        if ((exp - (Date.now()/1000)) < 300) {
          dispatch('refreshToken');
        }
      }
      if (refreshToken) {
        const decoded = jwt_decode(refreshToken);
        const exp = decoded.exp;
        if ((exp - (Date.now()/1000)) < 300) {
          commit('LOGOUT');
          this.$router.push('/signin');
        }
      }
      if (!refreshToken && !accessToken) {
        this.$router.push('/signin');
      }
    }
  },
  getters: {
    getUser(state) {
      return state.authUser
    },
    isAuthenticated(state) {
      return state.isAuthenticated
    },
    errorStatus(state) {
      return state.errorStatus
    }
  }
};

export default auth
