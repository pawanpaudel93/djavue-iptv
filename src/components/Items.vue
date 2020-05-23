<template>
    <mdb-container>
        <mdb-row>
            <mdb-col col="12" sm="6" lg="4" xl="3" v-for="item in items" :key="item.key">
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
    props: ['items', 'type']
  }
</script>
<style scoped>
    .list-group-item {
        margin-top: 15px;
    }
</style>