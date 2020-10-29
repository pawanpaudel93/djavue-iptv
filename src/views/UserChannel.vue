<template>
	<div>
		<mdb-container>
			<mdb-btn outline="info" @click.native="modalEnable = true">Add Channel<mdb-icon icon="fas fa-plus" class="ml-1"/></mdb-btn>
			<mdb-modal :show="modalEnable" @close="modalEnable = false">
			<mdb-modal-header class="text-center">
				<mdb-modal-title tag="h5" bold class="w-100">Enter Channel Info</mdb-modal-title>
			</mdb-modal-header>
			<form @submit.prevent="addChannel();">
				<mdb-modal-body class="mx-3 grey-text">
					<mdb-input
						label="Name*" 
						class="mb-5" 
						v-model="channel.name" 
						:customValidation="validated" 
						:isValid="$v.channel.name.required && $v.channel.name.$dirty && $v.channel.name.maxLength"
						invalidFeedback="Name is required!"
					/>
					<mdb-input
						label="URL*" 
						class="mb-5" 
						v-model="channel.url"
						:customValidation="validated"
						:isValid="$v.channel.url.required && $v.channel.url.$dirty && $v.channel.url.url && $v.channel.url.maxLength"
						:invalidFeedback="invalidError.url"
					/>
					<mdb-input
						label="Logo URL" 
						class="mb-5" 
						v-model="channel.logoUrl"
						:customValidation="validated" 
						:isValid="($v.channel.logoUrl.$model && $v.channel.logoUrl.url) && $v.channel.logoUrl.maxLength"
						:invalidFeedback="invalidError.logoUrl"
					/>
					<mdb-input
						label="Category"
						class="mb-5"
						v-model="channel.category"
						:customValidation="validated" 
						:isValid="$v.channel.url.$dirty && $v.channel.category.maxLength"
						:invalidFeedback="'Category is greater than max length: '+ $v.channel.category.$params.maxLength.max + '!'"
					/>
					<mdb-input
						label="Language"
						class="mb-5" 
						v-model="channel.language"
						:customValidation="validated" 
						:isValid="$v.channel.url.$dirty && $v.channel.language.maxLength"
						:invalidFeedback="'Language is greater than max length: '+ $v.channel.language.$params.maxLength.max +'!'"
					/>
					<mdb-input
						label="Country"
						class="mb-5"
						v-model="channel.country"
						:customValidation="validated" 
						:isValid="$v.channel.country.$dirty && $v.channel.country.maxLength"
						:invalidFeedback="'Country is greater than max length: '+ $v.channel.country.$params.maxLength.max + '!'"
					/>
				</mdb-modal-body>
				<mdb-modal-footer center>
					<mdb-btn type="submit" outline="info">Add <mdb-icon icon="fas fa-plus" class="ml-1"/></mdb-btn>
				</mdb-modal-footer>
			</form>
			</mdb-modal>
		</mdb-container>
		<Channels :tvInfos="tvInfos" :type="'default'"/>
		<notifications
			group="UserChannel"
			position="bottom right"
		/>
		<infinite-loading @infinite="infiniteHandler" spinner="waveDots"></infinite-loading>
	</div>
</template>

<script>
	import { mdbContainer, mdbTextarea, mdbIcon, mdbBtn, mdbModal, mdbModalHeader, mdbModalTitle, mdbModalBody, mdbInput, mdbModalFooter } from 'mdbvue';
	import { mapGetters } from 'vuex';
	import axios from '@/api/httpClient1';
	import Channels from "@/components/Channels.vue";
	import { required, maxLength, url } from "vuelidate/lib/validators";
	
	export default {
		name: 'UserChannel',
		components: {
			mdbContainer,
			mdbBtn,
			mdbModal,
			mdbModalHeader,
			mdbModalBody,
			mdbInput,
			mdbModalFooter,
			mdbTextarea,
			mdbIcon,
			mdbModalTitle,
			Channels
		},
		data() {
			return {
				page: 1,
				next: '',
				tvInfos: [],
				modalEnable: false,
				validated: false,
				channel: {
					name: "",
					url: "",
					logoUrl: "",
					category: "",
					language: "",
					country: ""
				},
				invalidError: {
					url: "",
					logoUrl: "",
				}
			}
		},
		validations: {
			channel: {
				name: { required, maxLength: maxLength(100)},
				url: { required, maxLength: maxLength(2083), url },
				logoUrl: { maxLength: maxLength(2083), url },
				category: { maxLength: maxLength(100)},
				language: { maxLength: maxLength(60)},
				country: { maxLength: maxLength(75)}
			}
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
			show (group, type = '', context = '') {
				const text = `
					${context}
					<br>
					Date: ${new Date()}
				`
				this.$notify({
					group,
					title: `Channel Notification`,
					text,
					type,
					data: {
					randomNumber: Math.random()
					}
				})
			},
			addChannel() {
				this.validated = true;
				if (!this.$v.channel.url.required || this.$v.channel.url.$dirty) {
					this.invalidError.url = "URL is required!"
				}
				else if (this.$v.channel.url.$dirty && !this.$v.channel.url.url) {
					this.invalidError.url = "Invalid URL!"
				}
				else if (this.$v.channel.url.$dirty && !this.$v.channel.url.maxLength) {
					this.invalidError.url = `URL length is greater than max length: ${$v.channel.url.$params.maxLength.max}!`
				}
				if (this.$v.channel.logoUrl.$dirty && !this.$v.channel.logoUrl.url) {
					this.invalidError.url = "Invalid URL!"
				}
				else if (this.$v.channel.logoUrl.$dirty && !this.$v.channel.logoUrl.maxLength) {
					this.invalidError.url = `URL length is greater than max length: ${$v.channel.url.$params.maxLength.max}!`
				}
				this.$v.$touch();
				if (!this.$v.$invalid) {
					let data = {
						name: this.channel.name,
						logo: this.channel.logoUrl,
						url: this.channel.url,
						category: this.channel.category,
						language: this.channel.language,
						country: this.channel.country
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
						// console.log(res);
						if (res.status == 201) {
							let tvId = this.tvInfos.map(item => item.id).indexOf(res.data.id);
							if (tvId == -1) {
								this.tvInfos.push(res.data);
							}
							this.show('UserChannel', 'success', `<b>${res.data.name}</b> channel successfully added!`);
							this.modalEnable = false;
							this.channel = {
								name: "",
								url: "",
								logoUrl: "",
								category: "",
								language: "",
								country: ""
							}
						}
					})
					.catch(error => {
						this.modalEnable = false;
						this.channel = {
								name: "",
								url: "",
								logoUrl: "",
								category: "",
								language: "",
								country: ""
							}
						if (error.response.data.error == "IntegrityError") {
							this.show('UserChannel', 'error', `Channel exists with the url given!`);
						}
						console.log(error.response.data);
						console.log(error.response.status);
						console.log(error.response.headers);
					})	
				}
			}
		},
		computed: {
			isError() {
				return 
			}
		}
	}
</script>