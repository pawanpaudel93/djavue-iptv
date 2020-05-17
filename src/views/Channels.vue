<template>
	<mdb-container>
		<br>
		<mdb-row>
			<mdb-col col="12" sm="6" lg="4" xl="3" v-for="tvInfo in newtvInfos" :key="tvInfo.id">
				<mdb-card>
					<mdb-view hover>
						<a href="#!">
							<mdb-card-image
								src="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%282%29.jpg"
								alt="Card image cap"/>
							<mdb-mask flex-center waves overlay="white-slight"></mdb-mask>
						</a>
					</mdb-view>
					<mdb-card-body>
						<mdb-card-title>{{ tvInfo.name}}</mdb-card-title>
						<mdb-card-text>
							Category: {{ tvInfo.category }}
							Country: {{ tvInfo.country }}
							Language: {{ tvInfo.language }}
						</mdb-card-text>
						<mdb-btn color="unique">Watch</mdb-btn>
					</mdb-card-body>
				</mdb-card>
			</mdb-col>
		</mdb-row>
		<div v-infinite-scroll="loadMore" infinite-scroll-disabled="busy" infinite-scroll-distance="10">...</div>			
	</mdb-container>
</template>

<style scoped>
	.card {
		margin-top: 20px;
	}
</style>
<script>
	import { mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText, mdbBtn, mdbView, mdbMask, mdbContainer, mdbRow, mdbCol } from 'mdbvue';
	import { mapGetters } from 'vuex';

	var count = 0;
	export default {
		name: 'Channels',
		data() {
			return {
				newtvInfos: [],
				busy: false
			}
		},
		components: {
			mdbCard,
			mdbCardImage,
			mdbCardBody,
			mdbCardTitle,
			mdbCardText,
			mdbBtn,
			mdbView,
			mdbMask,
			mdbContainer,
			mdbRow,
			mdbCol
		},
		computed: {
			...mapGetters({
			tvInfos: 'getTvInfos'
			})
		},
		  methods: {
			loadMore: function() {
				this.busy = true;

				setTimeout(() => {
					for (var i = 0, j = 50; i < j; i++) {
						this.newtvInfos.push(this.tvInfos[count++]);
					}
					this.busy = false;
				}, 1000);
			}
		},
		created() {
			if (this.$route.params.name == 'Unknown') {
				this.$store.dispatch('setTvInfos', {filterBy:this.$route.params.type, name: ""});
			} else {
				this.$store.dispatch('setTvInfos', {filterBy:this.$route.params.type, name: this.$route.params.name})
			}
		}
	}
</script>