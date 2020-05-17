<template>
  <div class="home">
    <NavBar/>
    <br>
    <span>Choosen By:</span>
    <!-- Group of default radios - option 1 -->
    <div class="custom-control custom-radio">
      <input type="radio" v-model="radioDefault" class="custom-control-input" id="country" name="country" value="country">
      <label class="custom-control-label" for="country">Country</label>
    </div>

    <!-- Group of default radios - option 2 -->
    <div class="custom-control custom-radio">
      <input type="radio" v-model="radioDefault" class="custom-control-input" id="category" name="category" value="category">
      <label class="custom-control-label" for="category">Category</label>
    </div>
    <Items :items="countries" v-if="radioDefault=='country'"/>
    <Items :items="categories" v-else/>
  </div>
</template>

<style scoped>

</style>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
import Items from "@/components/Items.vue";
import { mapGetters } from 'vuex'

export default {
  name: "Home",
  data() {
    return {
      radioDefault: 'country'
    }
  },
  components: {
    NavBar,
    Items
  },
  computed: {
    ...mapGetters({
      categories: 'getCategories',
      countries: 'getCountries'
    })
  },
  created () {
    this.$store.dispatch('setCategories');
    this.$store.dispatch('setCountries');
  }
};
</script>
