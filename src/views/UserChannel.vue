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
				const api = `/api/iptv/channels/?page=${this.page}`
				if (this.next !== null) {
					let config = {
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + localStorage.getItem("access"),
							'Cache-Control': 'no-cache'
						}
					}
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
	}
</script>