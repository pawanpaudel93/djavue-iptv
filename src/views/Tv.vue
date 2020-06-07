<template>
	<div>
		<Channels :tvInfos="tvInfos" :type="'default'"/>
		<infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'
	import axios from '@/api/httpClient'
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
				const api = (this.$route.params.name === 'Unknown')?`/api/iptv/channels/${this.$route.params.type}//?page=${this.page}`:`/api/iptv/channels/${this.$route.params.type}/${this.$route.params.name}/?page=${this.page}`
				if (this.next !== null) {
					axios.get(api)
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