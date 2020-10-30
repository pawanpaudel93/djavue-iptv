<template>
    <mdb-container>
    <mdb-row class="justify-content-md-center">
      <mdb-col md="5">
        <mdb-card>
          <mdb-card-body class="mx-4">
            <div class="text-center">
              <h3 class="dark-grey-text mb-5"><strong>Sign in</strong></h3>
            </div>
            <form @submit.prevent="signIn">
              <mdb-input
                v-model="username" 
                label="Your username" 
                type="text" 
                autocomplete="current-username"
                :customValidation="validated" 
                :isValid="$v.username.required && $v.username.$model"
                invalidFeedback="Username is required!"
              />
              <mdb-input
                v-model="password" 
                label="Your password" 
                type="password" 
                containerClass="mb-0" 
                autocomplete="current-password"
                :customValidation="validated" 
                :isValid="$v.password.required && $v.password.$model"
                invalidFeedback="Password is required!"
              />
              <p class="font-small blue-text d-flex justify-content-end pb-3">Forgot <a href="#" class="blue-text ml-1"> Password?</a></p>
              <div class="text-center mb-3">
                <mdb-btn type="submit" gradient="blue" rounded class="btn-block z-depth-1a">Sign in</mdb-btn>
              </div>
            </form>
          </mdb-card-body>
          <mdb-modal-footer class="mx-5 pt-3 mb-1">
            <p class="font-small grey-text d-flex justify-content-end">Not a member? <a @click="$router.push('/signup')" class="blue-text ml-1"> Sign Up</a></p>
          </mdb-modal-footer>
        </mdb-card>
      </mdb-col>
    </mdb-row>
    <br/>
    <p class="text-danger" v-if="error">{{ error }}</p>
  </mdb-container>
</template>

<style scoped>
  .container {
    margin-top: 30px;
  }
</style>

<script>
  import { mdbContainer, mdbRow, mdbCol, mdbCard, mdbCardBody, mdbInput, mdbBtn, mdbIcon, mdbModal, mdbModalBody, mdbModalFooter } from 'mdbvue';
  import { mapGetters } from 'vuex';
  import { required } from "vuelidate/lib/validators";

  export default {
    name: 'Signin',
    components: {
      mdbContainer,
      mdbRow,
      mdbCol,
      mdbCard,
      mdbCardBody,
      mdbInput,
      mdbBtn,
      mdbIcon,
      mdbModal,
      mdbModalBody,
      mdbModalFooter
    },
    data() {
      return {
        username: '',
        password: '',
        validated: false
      };
    },
    computed: {
      ...mapGetters({
        error: 'errorStatus',
      })
    },
    methods: {
      signIn() {
        this.validated = true;
        this.$v.$touch();
        const credentials = {
          username: this.username,
          password: this.password
        }
        this.$store.dispatch("obtainToken", credentials);
        // this.$router.push("/");
      }
    },
    validations: {
      username: { required },
      password: { required }
    }
  }
</script>