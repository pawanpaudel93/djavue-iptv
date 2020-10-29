<template>
    <div>
        <br>
        <span>Parse By:</span>
        <div>
            <div class="custom-control custom-radio custom-control-inline">
                <input type="radio" v-model="radioDefault" class="custom-control-input" id="File" name="File" value="File">
                <label class="custom-control-label" for="File">File</label>
            </div>
            <div class="custom-control custom-radio custom-control-inline">
                <input type="radio" v-model="radioDefault" class="custom-control-input" id="URL" name="URL" value="URL">
                <label class="custom-control-label" for="URL">URL</label>
            </div>
        </div>
        <div class="container" v-if="radioDefault=='File'">
            <div class="form">
                <div class="large-12 medium-12 small-12 cell">
                    <div class="file-upload-wrapper" :data-text="fileText" ref="filewrapper">
                        <input type="file" id="file" ref="file" @change="handleFileUpload()" class="file-upload-field" value=""/>
                    </div>
                    <!-- <mdb-btn outline="success" v-on:click="submitFile()">UPLOAD</mdb-btn> -->
                </div>
            </div>
        </div>
        <mdb-input label="Enter Url" size="lg" v-if="radioDefault=='URL'" class="center" v-model="url"/>
        <mdb-btn outline="primary" tag="a" @click="handleUrl" v-if="radioDefault=='URL'" :disabled="$v.url.$model && !$v.url.url">Parse</mdb-btn>
        <br/><p style="float: right; margin-right: 150px; margin-top: 10px;">Total Channels: {{ tvInfos.length }}</p>
        <Channels :tvInfos="chunktvInfos" :type="'custom'"/>
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots" v-if="tvInfos.length!=0"></infinite-loading>
    </div>
</template>

<style scoped>
    @import url(https://fonts.googleapis.com/css?family=Lato:400,700,300);
    body {
        font-family: 'Lato', sans-serif;
    }
    .container {
        display: flex;
        -webkit-box-pack: center;
        -moz-box-pack: center;
        box-pack: center;
        -webkit-justify-content: center;
        -moz-justify-content: center;
        -ms-justify-content: center;
        -o-justify-content: center;
        justify-content: center;
        -ms-flex-pack: center;
    }
    .center {
        margin: auto;
        width: 50%;
    }
    .form {
        width: 400px;
    }
    .container {
        padding-top: 30px;
    }
    .file-upload-wrapper {
        position: relative;
        width: 100%;
        height: 60px;
        border-bottom: 1px solid #4285f4;
    }
    .file-upload-wrapper:after {
        content: attr(data-text);
        font-size: 18px;
        position: absolute;
        top: 0;
        left: 0;
        background: #fff;
        padding: 10px 15px;
        display: block;
        width: calc(100% - 40px);
        pointer-events: none;
        z-index: 20;
        height: 40px;
        line-height: 40px;
        color: #999;
        border-radius: 5px 10px 10px 5px;
        font-weight: 300;
    }
    .file-upload-wrapper:before {
        content: 'Upload';
        position: absolute;
        top: 0;
        right: 0;
        display: inline-block;
        height: 60px;
        background:#4285f4;
        color: #fff;
        font-weight: 700;
        z-index: 25;
        font-size: 16px;
        line-height: 60px;
        padding: 0 15px;
        text-transform: uppercase;
        pointer-events: none;
        border-radius: 0 5px 5px 0;
    }
    .file-upload-wrapper:hover:before {
        background: blue;
    }
    .file-upload-wrapper input {
        opacity: 0;
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        z-index: 99;
        height: 40px;
        margin: 0;
        padding: 0;
        display: block;
        cursor: pointer;
        width: 100%;
    }
</style>

<script>
    import { mdbBtn, mdbContainer, mdbRow, mdbCol, mdbInput } from "mdbvue";
    import { required, maxLength, url} from 'vuelidate/lib/validators'
    import axios from "@/api/httpClient"
    import Channels from "@/components/Channels.vue"
    
    export default {
        name: "ParseM3u",
        data(){
            return {
                file: '',
                fileText: "Select your file!",
                tvInfos: [],
                chunktvInfos: [],
                channelStep: 20,
                radioDefault: 'File',
                url: ''
            }
        },
        components: {
            mdbBtn,
            mdbContainer,
            mdbRow,
            mdbCol,
            mdbInput,
            Channels
        },
        methods: {
            submitFile(){
                let formData = new FormData();
                formData.append('file', this.file);

                axios.post( '/api/parsem3u',
                    formData,
                    {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }
                ).then(res => {
                    this.tvInfos = res.data;
                    this.fileText = "Select your file!"
                })
                .catch(err =>{
                    console.log(err.response);
                    this.fileText = "Select your file!"
                });
            },
            handleFileUpload() {
                this.file = this.$refs.file.files[0];
                this.fileText = this.file.name;
                this.tvInfos = []
                this.chunktvInfos = []
                this.submitFile();
            },
            handleUrl() {
                this.tvInfos = []
                this.chunktvInfos = []
                axios.get('/api/parsem3u', {
                    params: {
                        url: this.url
                    }
                })
                .then( res => {
                    this.tvInfos = res.data;
                })
                .catch(err => {
                    console.log(err.response);
                })
            },
            infiniteHandler($state) {
                if (this.chunktvInfos.length === 0) {
                    this.chunktvInfos.push(...this.tvInfos.slice(this.chunktvInfos.length, this.chunktvInfos.length + this.channelStep));
                    $state.loaded();
                }
				else if (this.chunktvInfos.length < this.tvInfos.length) {
                    this.chunktvInfos.push(...this.tvInfos.slice(this.chunktvInfos.length, this.chunktvInfos.length + this.channelStep));
                    $state.loaded();
				}
				else {
					$state.complete();
				}
			},
        },
        validations: {
			url: {
				required,
				maxLength: maxLength(2083),
				url
			},
		}
    }
</script>