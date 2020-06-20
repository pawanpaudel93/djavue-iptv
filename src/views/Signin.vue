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
              <mdb-input v-model="username" label="Your email" type="email" required/>
              <mdb-input v-model="password" label="Your password" type="password" containerClass="mb-0" required/>
              <p class="font-small blue-text d-flex justify-content-end pb-3">Forgot <a href="#" class="blue-text ml-1"> Password?</a></p>
              <div class="text-center mb-3">
                <mdb-btn type="submit" gradient="blue" rounded class="btn-block z-depth-1a">Sign in</mdb-btn>
              </div>
            </form>
          </mdb-card-body>
          <mdb-modal-footer class="mx-5 pt-3 mb-1">
            <p class="font-small grey-text d-flex justify-content-end">Not a member? <a href="#" class="blue-text ml-1"> Sign Up</a></p>
          </mdb-modal-footer>
        </mdb-card>
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
        showModal: false,
        username: '',
        password: ''
      };
    }
  }
</script>