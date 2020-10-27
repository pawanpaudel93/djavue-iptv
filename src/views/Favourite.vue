<template>
	<div>
		<Channels :tvInfos="tvInfos" :type="'default'"/>
		<infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import axios from '@/api/httpClient1'
	import Channels from "@/components/Channels.vue"

	export default {
		name: 'Tv',
		data() {
			return {
				page: 1,
				next: '',
				tvInfos: [],
			}
		},
		components: {
			Channels
		},
		  methods: {
			infiniteHandler($state) {
				let config = {
					headers: {
						"Content-Type": "application/json",
						"Authorization": "Bearer " + localStorage.getItem("access"),
						'Cache-Control': 'no-cache'
					}
				}
				const api = `/api/accounts/favourites/?page=${this.page}`
				if (this.next !== null) {
					axios.get(api, config)
						.then(({ data }) => {
							if (data.results.length) {
								this.next = data.next;
								this.page += 1;
								this.tvInfos.push(...data.results);
								$state.loaded();
							} else {
								$state.complete();
							}
						})
						.catch(error => {
							$state.complete();
						});
				}
				else {
					$state.complete();
				}
			},
		},
		computed: {
			...mapGetters({
				isAuthenticated: "isAuthenticated"
			})
		},
		created () {
			if (this.isAuthenticated) {
				this.$store.dispatch('setFavourites');
			}
		}
	}
</script>