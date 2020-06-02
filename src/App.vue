<template>
  <div id="app">
    <NavBar v-if="$route.name!='test1'"></NavBar>
    <br><br><br>
    <transition
      name="fade"
      mode="out-in"
     >
      <router-view :key="$route.path" style="padding-bottom: 5.5rem;"></router-view>
    </transition>
    <Footer v-if="$route.name!='test1'"/>
  </div>
</template>

<script>
  import NavBar from "@/components/NavBar.vue";
  import Footer from "@/components/Footer.vue";
  export default {
    components: {
      NavBar,
      Footer
    },
    methods: {
      beforeLeave(element) {
        this.prevHeight = getComputedStyle(element).height;
      },
      enter(element) {
        const { height } = getComputedStyle(element);

        element.style.height = this.prevHeight;

        setTimeout(() => {
          element.style.height = height;
        });
      },
      afterEnter(element) {
        element.style.height = 'auto';
      },
    }
  }
</script>
<style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    position: relative;
    min-height: 100vh;
  }

  #nav {
    padding: 30px;
  }

  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }

  #nav a.router-link-exact-active {
    color: #42b983;
  }
  .fade-enter-active,
  .fade-leave-active {
    transition-duration: 0.3;
    transition-property: opacity;
    transition-timing-function: ease;
    overflow: hidden;
  }

  .fade-enter,
  .fade-leave-active {
    opacity: 0
  }
</style>
