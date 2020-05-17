<template>
    <mdb-container>
        <mdb-row>
            <mdb-col col="12" sm="6" lg="4" xl="3" v-for="item in items" :key="item.key">
                <mdb-list-group-item :action="true" v-if="item.key!=''"> {{item.key}} <mdb-badge color="primary" pill>{{ item.counts }}</mdb-badge></mdb-list-group-item>
                <mdb-list-group-item :action="true" v-else> Unknown <mdb-badge color="primary" pill>{{ item.counts }}</mdb-badge></mdb-list-group-item>
            </mdb-col>
        </mdb-row>
    </mdb-container>
</template>

<script>
  import { mdbContainer, mdbListGroupItem, mdbBadge, mdbRow, mdbCol} from 'mdbvue';
  export default {
    name: 'Items',
    components: {
      mdbContainer,
      mdbListGroupItem,
      mdbBadge,
      mdbRow,
      mdbCol
    },
    props: ['items']
  }
</script>
<style scoped>
    .list-group-item {
        margin-top: 15px;
    }
</style>