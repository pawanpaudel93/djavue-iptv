<template>
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
        <mdb-input label="Enter m3u8 Url" v-model="url" size="lg"/>
		<mdb-btn outline="primary" tag="a" @click="setVideoUrl(url)" data-toggle="modal" data-target="#video-modal" :disabled="!$v.url.checkUrl">Watch</mdb-btn>
    </mdb-container>
</template>


<style scoped>
	#arrow {
		float: left;
		margin-left:50px;
		margin-top:20px;
	}
</style>
<script>
	import {
            mdbBtn, mdbView, mdbMask, mdbContainer, mdbRow, mdbCol, mdbInput, mdbIcon, mdbModal,
            mdbModalHeader, mdbModalTitle, mdbModalBody, mdbModalFooter, mdbNavItem
			} from 'mdbvue'
	import { required,maxLength} from 'vuelidate/lib/validators'
	import Player from "@/components/Player.vue"

	const checkUrl = (value) => {
		let regexp = /^(?:(?:https?|ftp):\/\/)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,})))(?::\d{2,5})?(?:\/\S*)?$/;
		return regexp.test(value)? true:false;
	}
	export default {
		name: 'PlayUrl',
		data() {
			return {
				showModal: false,
                videoUrl: '',
                url: ''
			}
		},
		components: {
			mdbBtn,
			mdbView,
			mdbMask,
            mdbContainer,
            mdbInput,
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
		},
		methods: {
			setVideoUrl(url) {
				let protocol = new URL(url).protocol;
				this.videoUrl =  url;
				this.showModal=true;
				console.log(protocol, location.protocol);
				if ((process.env.NODE_ENV === "production") && (protocol !== location.protocol) && (location.protocol !== 'http:')) {
					localStorage.removeItem("url");
					localStorage.setItem('url', this.videoUrl);
					location.href = location.href.replace(location.protocol, protocol);
				}
			}
		},
		validations: {
			url: {
				required,
				maxLength: maxLength(2083),
				checkUrl
			},
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