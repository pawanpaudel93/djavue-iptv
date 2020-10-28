<template>
	<div>
		<br>
		<a @click="$router.go(-1)" id="arrow"><i class="fa fa-arrow-left fa-3x"></i></a>
		<mdb-container>
			<br><br>
			<mdb-modal size="lg" :show="showModal" @close="showModal=false" info>
				<mdb-modal-body class="mb-0 p-0">
					<Player :source="videoUrl"/>
					<!-- <div class="embed-responsive embed-responsive-16by9 z-depth-1-half"> -->
						<!-- <iframe class="embed-responsive-item" :src="videoUrl" allowfullscree></iframe> -->
					<!-- </div> -->
				</mdb-modal-body>
				<mdb-modal-footer class="justify-content-center">
					<span class="mr-4">Spread the word! <i><b>"DjaVue IPTV"</b></i></span>
					<a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
					<a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
					<a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
					<a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
					<mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal = false">Close</mdb-btn>
				</mdb-modal-footer>
			</mdb-modal>
			<mdb-row>
				<mdb-col col="12" sm="6" lg="4" xl="3" v-for="tvInfo in tvInfos" :key="tvInfo.id" style="margin-top: 20px">
					<mdb-card class="h-100 border-primary">
						<mdb-view hover cascade>
							<a href="#!">
								<v-lazy-image
									:src="tvInfo.logo"
									src-placeholder="https://mdbootstrap.com/img/Photos/Horizontal/Nature/4-col/img%20%282%29.jpg"
									:alt="tvInfo.name" class="img-fluid"/>
								<mdb-mask flex-center waves overlay="white-slight"></mdb-mask>
							</a>
						</mdb-view>
						<mdb-card-body>
							<mdb-card-title>{{ tvInfo.name }}</mdb-card-title>
							<mdb-card-text v-if="type=='default'">
								Category: {{ tvInfo.category }}<br>
								Country: {{ tvInfo.country }}<br>
								Language: {{ tvInfo.language }}
							</mdb-card-text>
							<mdb-card-text v-if="type=='custom'">
								Category: {{ tvInfo.category }}<br>
								Country: {{ tvInfo.country.name }}<br>
								Language: {{ tvInfo.language.name }}
							</mdb-card-text>
							<mdb-btn color="unique" tag="a" @click="setVideoUrl(tvInfo.url)" data-toggle="modal" data-target="#video-modal">Watch</mdb-btn>
							<div v-if="isAuthenticated && $route.path !== '/parsem3u'" style="display: inline; margin-left: 5px;">
								<a @click="unfavourite(tvInfo)" v-if="favourites.includes(tvInfo.id)"><mdb-icon icon="heart" class="red-text pr-1" style="font-size: 1.5em;"/></a>
								<a @click="favourite(tvInfo)" v-else><mdb-icon far icon="heart" style="font-size: 1.5em;"/></a>
							</div>
							<div v-if="isAuthenticated" style="display: inline; margin-left: 5px;">
								<button type="button" v-if="$route.path=='/parsem3u'" :ref="tvInfo.name" @click="addChannel(tvInfo)" class="btn btn-outline-info waves-effect">Add</button>
								<a v-if="$route.path=='/mychannels'" @click="removeChannel(tvInfo)"><i class="fas fa-trash" style="font-size:23px;"></i></a>
							</div>
						</mdb-card-body>
					</mdb-card>
				</mdb-col>
			</mdb-row>
		</mdb-container>
	</div>
</template>


<style scoped>
	.view {
		height: 150px;
	}
	.view img {
		height: 100%;
		width: 100%;
	}
	.v-lazy-image {
		filter: blur(7px);
		transition: filter 0.7s;
		transition-timing-function: ease;
	}
	.v-lazy-image-loaded {
		filter: blur(0);
	}
	#arrow {
		float: left;
		margin-left:50px;
		margin-top:20px;
		/* position: fixed; */
    	/* top: 70px; */
		/* right: 5px; */
		/* left: 0px; */
	}
</style>
<script>
	import { 
			mdbCard, mdbCardImage, mdbCardBody, mdbCardTitle, mdbCardText, 
			mdbBtn, mdbView, mdbMask, mdbContainer, mdbRow, mdbCol,
			mdbIcon, mdbModal, mdbModalHeader, mdbModalTitle, mdbModalBody, 
			mdbModalFooter, mdbNavItem
			} from 'mdbvue'
	import { mapGetters } from 'vuex'
	import axios from '@/api/httpClient1'
	import Player from "@/components/Player.vue"
	import VLazyImage from "v-lazy-image";

	export default {
		name: 'Channels',
		data() {
			return {
				showModal: false,
				videoUrl: '',
				states: {}
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
			mdbCol,
			// for modal
			mdbIcon,
			mdbModal,
			mdbModalHeader,
			mdbModalTitle,
			mdbModalBody,
			mdbModalFooter,
			mdbBtn,
			mdbNavItem,
			// tv player
			Player,
			// image lazy loader
			VLazyImage
		},
		  methods: {
			setVideoUrl(url) {
				this.videoUrl = url;
				this.showModal=true;
				let protocol = new URL(this.videoUrl).protocol;
				console.log(protocol, location.protocol);
				if ((process.env.NODE_ENV === "production") && (protocol !== location.protocol) && (location.protocol !== 'http:')) {
					localStorage.removeItem("url");
					localStorage.setItem('url', this.videoUrl);
					location.href = location.href.replace(location.protocol, protocol);
				}
			},
			favourite(tvInfo) {
				console.log(this.buttons[tvInfo.id]);
				let config = {
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + localStorage.getItem("access"),
							'Cache-Control': 'no-cache'
						}
					}
				axios.post('/api/iptv/fav-unfav', {
					"action": "fav",
					"channel_id": tvInfo.id
				}, config)
				.then(res => {
					// console.log(res)
					if (res.data.status == "success") {
						// console.log("fav")
						this.favourites.push(tvInfo.id);
						this.$store.commit('SET_FAVOURITES', this.favourites);
						this.buttons[tvInfo.id] = true;
					}
				})
				.catch(error => {
					console.log(error)
				})
			},
			unfavourite(tvInfo) {
				console.log(this.buttons[tvInfo.id]);
				let config = {
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + localStorage.getItem("access"),
							'Cache-Control': 'no-cache'
						}
					}
				axios.post('/api/iptv/fav-unfav', {
					"action": "unfav",
					"channel_id": tvInfo.id
				}, config)
				.then(res => {
					// console.log(res);
					if (res.data.status == "success") {
						// console.log("unfav")
						let id = this.favourites.indexOf(tvInfo.id);
						if ( id != -1) {
							this.favourites.splice(id, 1);
						}
						this.$store.commit('SET_FAVOURITES', this.favourites);
						if (location.pathname === "/favourites") {
							let tvId = this.tvInfos.map(item => item.id).indexOf(tvInfo.id);
							if (tvId != -1) {
								this.tvInfos.splice(tvId, 1);
							}
						}
						this.buttons[tvInfo.id] = false;
					}
				})
				.catch(error => {
					console.log(error)
				})
			},
			addChannel(tvInfo) {
				let data = {
					name: tvInfo.name,
					logo: tvInfo.logo,
					url: tvInfo.url,
					category: tvInfo.category,
					language: tvInfo.language.name,
					country: tvInfo.country.name
				}
				let config = {
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + localStorage.getItem("access"),
							'Cache-Control': 'no-cache'
						}
					}
				axios.post("/api/iptv/channels/", JSON.stringify(data), config)
				.then(res => {
					console.log(res);
					if (res.status == 201) {
						this.$refs[tvInfo.name][0].disabled = true;
						this.$refs[tvInfo.name][0].innerText = "Added";
					}
				})
				.catch(error => {
					// console.log(error.response.data);
					// console.log(error.response.status);
					// console.log(error.response.headers);
					if (error.response.status == 500 && error.response.data.error == "IntegrityError") {
						this.$refs[tvInfo.name][0].disabled = true;
						this.$refs[tvInfo.name][0].innerText = "Added";
					}
				})
			},
			removeChannel(tvInfo) {
				let config = {
						headers: {
							"Content-Type": "application/json",
							"Authorization": "Bearer " + localStorage.getItem("access"),
							'Cache-Control': 'no-cache'
						}
					}
				axios.delete(`/api/iptv/channels/${tvInfo.id}`, config)
				.then(res => {
					if (res.status == 204) {
						let tvId = this.tvInfos.map(item => item.id).indexOf(tvInfo.id);
						if (tvId != -1) {
							this.tvInfos.splice(tvId, 1);
						}
					}
				})
				.catch(error => {
					console.log(error);
				})
			}
		},
		props: ["tvInfos", "type"],
		computed: {
			buttons: function () {
				this.states = {...this.states, ...this.tvInfos.reduce((acc, tvInfo) => ({...acc, [tvInfo.id]: false}),{})}
				return this.states;
			},
			...mapGetters({
				isAuthenticated: 'isAuthenticated',
				favourites: 'getFavourites'
			})
		},
		mounted() {
			this.$nextTick(() => {
				let url = localStorage.getItem('url');
				if (url) {
					this.videoUrl = url;
					this.showModal=true;
					localStorage.removeItem("url");
				}
			})
		}
	}
</script>