<template>
	<div>
		<br>
		<a @click="$router.go(-1)" id="arrow"><i class="fa fa-arrow-left fa-3x"></i></a>
		<mdb-container>
			<br><br>
			<mdb-modal size="lg" :show="showModal" @close="showModal=false" info>
				<mdb-modal-body class="mb-0 p-0">
					<!-- <Player :source="videoUrl"/> -->
					<div class="embed-responsive embed-responsive-16by9 z-depth-1-half">
						<iframe class="embed-responsive-item" :src="videoUrl" allowfullscree></iframe>
					</div>
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
						</mdb-card-body>
					</mdb-card>
				</mdb-col>
			</mdb-row>
			<!-- <infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading> -->
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
			mdbIcon, mdbModal, mdbModalHeader, mdbModalTitle, mdbModalBody, mdbModalFooter, mdbNavItem
			} from 'mdbvue'
	import { mapGetters } from 'vuex'
	import axios from 'axios'
	import Player from "@/components/Player.vue"
	import VLazyImage from "v-lazy-image";

	export default {
		name: 'Channels',
		data() {
			return {
				showModal: false,
				videoUrl: ''
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
				let protocol = new URL(url).protocol;
				this.videoUrl = "https:" + process.env.VUE_APP_BASEURL + '/player?url=' + url;
				this.showModal=true;
				// this.videoUrl = url;
				// this.showModal=true;
				// localStorage.removeItem("url");
				// let protocol = new URL(this.videoUrl).protocol;
				// console.log(protocol, location.protocol);
				// if ((process.env.NODE_ENV === "production") && (protocol !== location.protocol)) {
				// 	localStorage.setItem('url', this.videoUrl);
				// 	location.href = location.href.replace(location.protocol, protocol);
				// }
			}
		},
		props: ["tvInfos", "type"],
		// mounted() {
		// 	this.$nextTick(() => {
		// 		let url = localStorage.getItem('url');
		// 		if (url) {
		// 			this.videoUrl = url;
		// 			this.showModal=true;
		// 			localStorage.removeItem("url");

		// 		}
		// 	})
		// }
	}
</script>