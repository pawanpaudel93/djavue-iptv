<template>
  <mdb-container>
    <mdb-row class="justify-content-md-center">
      <mdb-col style="padding-top: 10px;">
        *Username: <p class="text-secondary"> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</p>
        *Password:<p class="text-secondary"> Password must contain at least eight characters.</p>
      </mdb-col>
      <mdb-col md="5">
        <mdb-card>
          <mdb-card-body class="mx-4">
            <div class="text-center">
              <h3 class="dark-grey-text mb-5"><strong>Sign up</strong></h3>
            </div>
            <form @submit.prevent="signUp">
              <mdb-input 
                v-model="username" 
                label="Your username" 
                type="text" 
                autocomplete="new-username"
                required
              />
              <mdb-input 
                v-model="email" 
                label="Your email" 
                type="email" 
                autocomplete="new-email"
                required
              />
              <mdb-input 
                v-model="password" 
                label="Your password" 
                type="password" 
                autocomplete="new-password"
                required
              />
              <mdb-input 
                v-model="repeatPassword"
                label="Confirm your password"
                type="password"
                autocomplete="new-password"
                required
              />
              <div class="text-center mt-4">
                <mdb-btn type="submit" gradient="blue" rounded class="btn-block z-depth-1a" :disabled="password.length < $v.password.$params.minLength.min || password !== repeatPassword">Sign up</mdb-btn>
              </div>
            </form>
          </mdb-card-body>
          <mdb-modal-footer>
          </mdb-modal-footer>
        </mdb-card>
      </mdb-col>
      <mdb-col style="margin-top: 10px;">
        <!-- <p>{{$v}}</p> -->
        <p class="text-success" v-if="status">{{ status }}</p>
        <p class="text-danger" v-if="$v.username.maxLength===false">*Username field has more than {{$v.username.$params.maxLength.max}} charracters.</p>
        <p class="text-danger" v-if="$v.password.minLength===false">*Password must have at least {{$v.password.$params.minLength.min}} charracters.</p>
        <p class="text-danger" v-if="$v.repeatPassword.sameAsPassword===false">*Passwords must be identical.</p>
        <p class="text-danger" v-for="e in errorUsername" v-bind:key="e">{{ e }}</p>
        <p class="text-danger" v-for="e in errorPassword" v-bind:key="e">{{ e }}</p>
        <p class="text-danger" v-for="e in errorEmail" v-bind:key="e">{{ e }}</p>
      </mdb-col>
    </mdb-row>
  </mdb-container>
</template>

<style scoped>
  .container {
    margin-top: 30px;
  }
</style>

<script>
  import { mdbContainer, mdbRow, mdbCol, mdbCard, mdbCardBody, mdbInput, mdbBtn, mdbIcon, mdbModal, mdbModalBody, mdbModalFooter } from 'mdbvue';
  import axios from '@/api/httpClient1'
  import { required, minLength, maxLength, sameAs } from 'vuelidate/lib/validators'
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
        showModel: false,
        email: '',
        username: '',
        password: '',
        repeatPassword: '',
        errorUsername: '',
        errorPassword: '',
        errorEmail: '',
        status: ''
      };
    },
    methods: {
      signUp () {
        axios.post("auth/users/", {
          username: this.username,
          email: this.email,
          password: this.password
        })
          .then(res => {
            console.log(res);
            this.username = this.email = this.password = this.repeatPassword = "";
            this.errorUsername = this.errorPassword = this.errorEmail = "";
            this.status = "Congratulations!!! Account has been created."
            this.$router.push('/signin');
          })
          .catch(err => {
            console.log(err.response.data);
            this.errorUsername = err.response.data.username;
            this.errorPassword = err.response.data.password;
            this.errorEmail = err.response.data.email;
            setTimeout(()=>{
              this.errorUsername = this.errorPassword = this.errorEmail = "";
            }, 5000)
          })
      }
    },
    validations: {
      username: {
        required,
        maxLength: maxLength(150)
      },
      password: {
        required,
        minLength: minLength(8)
      },
      repeatPassword: {
        required,
        minLength: minLength(8),
        sameAsPassword: sameAs('password')

      }
    }
  }
</script>