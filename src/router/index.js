import Vue from "vue";
import store from '@/store/index';
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/signin",
    name: "signin",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import("@/views/Signin.vue"),
    beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next('/');
      } else {
        next();
      }
    }
  },
  {
    path: "/signup",
    name: "signup",
    component: () =>
      import("@/views/Signup.vue"),
    beforeEnter: (to, from, next) => {
      if (store.getters.isAuthenticated) {
        next('/');
      } else {
        next();
      }
    }
  },
  {
    path: "/:type/:name",
    name: "Tv",
    component: () =>
      import("@/views/Tv.vue")
  },
  {
    path: "/playurl",
    name: "PlayUrl",
    component: () =>
      import("@/views/PlayUrl.vue")
  },
  {
    path: "/parsem3u",
    name: "ParseM3u",
    component: () =>
      import("@/views/ParseM3u.vue")
  },
  {
    path: "/favourites",
    name: "Favourites",
    component: () =>
      import("@/views/Favourite.vue"),
    beforeEnter: (to, from, next) => {
      store.dispatch("inspectToken");
      if (!store.getters.isAuthenticated) {
        next('/signin');
      } else {
        next();
      }
    }
  },
  {
    path: "/mychannels",
    name: "Mychannels",
    component: () =>
      import("@/views/UserChannel.vue"),
    beforeEnter: (to, from, next) => {
      store.dispatch("inspectToken");
      if (!store.getters.isAuthenticated) {
        next('/signin');
      } else {
        next();
      }
    }
  }
];

const router = new VueRouter({
  mode: "history",
  // base: process.env.BASE_URL,
  routes
});

export default router;
