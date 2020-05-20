<template>
	<mdb-container>
		<br>
		<mdb-modal size="lg" :show="showModal" @close="showModal=false" info>
          <mdb-modal-body class="mb-0 p-0">
			<Player :source="videoUrl"></Player>
          </mdb-modal-body>
          <mdb-modal-footer class="justify-content-center">
            <span class="mr-4">Spread the word! <i><b>"DjaVue IPTV"</b></i></span>
            <a class="btn-floating btn-sm btn-fb"><i class="fab fa-facebook"></i></a>
            <!--Twitter-->
            <a class="btn-floating btn-sm btn-tw"><i class="fab fa-twitter"></i></a>
            <!--Google +-->
            <a class="btn-floating btn-sm btn-gplus"><i class="fab fa-google-plus"></i></a>
            <!--Linkedin-->
            <a class="btn-floating btn-sm btn-ins"><i class="fab fa-linkedin-in"></i></a>
            <mdb-btn outline="primary" rounded size="md" class="ml-4" @click.native="showModal = false">Close</mdb-btn>
          </mdb-modal-footer>
        </mdb-modal>
		<mdb-row>
			<mdb-col col="12" sm="6" lg="4" xl="3" v-for="tvInfo in tvInfos" :key="tvInfo.id">
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
						<mdb-card-title>{{ tvInfo.name }}</mdb-card-title>
						<mdb-card-text>
							Category: {{ tvInfo.category }}
							Country: {{ tvInfo.country }}
							Language: {{ tvInfo.language }}
						</mdb-card-text>
						<mdb-btn color="unique" tag="a" @click="setVideoUrl(tvInfo.url)" data-toggle="modal" data-target="#video-modal">Watch</mdb-btn>
					</mdb-card-body>
				</mdb-card>
			</mdb-col>
		</mdb-row>
		<infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
	</mdb-container>
</template>


<style scoped>
	.card {
		margin-top: 20px;
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

	export default {
		name: 'Channels',
		data() {
			return {
				page: 1,
				next: '',
				tvInfos: [],
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

			Player
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
			setVideoUrl(url) {
				this.videoUrl = url;
				this.showModal=true;
			}
		},
	}
</script>