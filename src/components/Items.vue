<template>
    <mdb-container>
        <mdb-row style="display: inline-block;">
          <mdb-form-inline class="md-form active-cyan-2 float-center">
            <mdb-input type="text" placeholder="Search" aria-label="Search" v-model="search"/>
            <mdbIcon icon="search" />
          </mdb-form-inline>
        </mdb-row>
        <mdb-row>
            <mdb-col col="12" sm="6" lg="4" xl="3" v-for="item in filteredItems" :key="item.key">
                <router-link :to="{ name: 'Tv', params: { type: type, name: item.key }}" v-if="item.key!==''">
                  <mdb-list-group-item :action="true"> 
                    {{item.key}}
                    <mdb-badge color="primary" pill>{{ item.counts }}</mdb-badge>
                  </mdb-list-group-item>
                </router-link>
                <router-link :to="{ name: 'Tv', params: { type: type, name: 'Unknown' }}" v-else>
                  <mdb-list-group-item :action="true">
                    Unknown
                  <mdb-badge color="primary" pill>{{ item.counts }}</mdb-badge>
                  </mdb-list-group-item>
                </router-link>
            </mdb-col>
        </mdb-row>
    </mdb-container>
</template>

<script>
  import { mdbContainer, mdbListGroupItem, mdbBadge, mdbRow, mdbCol, mdbIcon, mdbFormInline, mdbInput} from 'mdbvue';
  export default {
    name: 'Items',
    data() {
      return {
        search: ''
      }
    },
    components: {
      mdbContainer,
      mdbListGroupItem,
      mdbBadge,
      mdbRow,
      mdbCol,
      mdbIcon,
      mdbFormInline,
      mdbInput
    },
    props: ['items', 'type'],
    computed: {
      filteredItems() {
        if (this.search) {
          return this.items.filter(item => {
            return item.key.toLowerCase().includes(this.search.toLowerCase())
          })
        }
        else {
          return this.items;
        }
      }
    }
  }
</script>

<style scoped>
    .list-group-item {
        margin-top: 15px;
    }
    .active-cyan-2 input[type=text]:focus:not([readonly]) {
        border-bottom: 1px solid #4dd0e1;
        box-shadow: 0 1px 0 0 #4dd0e1;
    }
   .active-cyan-2 .fa {
        color: #4dd0e1;
    }
    .md-form {
      margin: 0px;
    }
</style>