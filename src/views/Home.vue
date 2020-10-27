<template>
  <div class="home">
    <br>
    <span>View By:</span>
    <!-- Group of radios-->
    <div>
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" v-model="radioDefault" class="custom-control-input" id="country" name="country" value="country">
        <label class="custom-control-label" for="country">Country</label>
      </div>
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" v-model="radioDefault" class="custom-control-input" id="category" name="category" value="category">
        <label class="custom-control-label" for="category">Category</label>
      </div>
      <div class="custom-control custom-radio custom-control-inline">
        <input type="radio" v-model="radioDefault" class="custom-control-input" id="language" name="language" value="language">
        <label class="custom-control-label" for="language">Language</label>
      </div>
    </div>
    <Items :items="countries" :type="radioDefault" v-if="radioDefault=='country'"/>
    <Items :items="categories" :type="radioDefault" v-if="radioDefault=='category'"/>
    <Items :items="languages" :type="radioDefault" v-if="radioDefault=='language'"/>
  </div>
</template>

<style scoped>

</style>

<script>
// @ is an alias to /src
import Items from "@/components/Items.vue";
import { mapGetters } from 'vuex';

export default {
  name: "Home",
  components: {
    Items
  },
  computed: {
    ...mapGetters({
      categories: 'getCategories',
      countries: 'getCountries',
      languages: 'getLanguages',
      isAuthenticated: "isAuthenticated"
    }),
    radioDefault: {
      get: function() {
        return this.$store.getters.getRadioDefault;
      },
      set: function(value) {
        this.$store.commit('SET_RADIO', value);
      }
    }
  },
  created () {
    this.$store.dispatch('setCountries');
    this.$store.dispatch('setCategories');
    this.$store.dispatch('setLanguages');
  }
};
</script>
