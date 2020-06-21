import axios from 'axios'
import { throttleAdapterEnhancer } from 'axios-extensions'

const throttleConfig = {
    threshold: 1800*1000 // 30 minutes
}

const httpClient = axios.create({
    baseUrl: process.env.VUE_APP_BASE_URL,
    timeout: 5000, // indicates, 1000ms ie. 1 second
    headers: {
        "Content-Type": "application/json",
        "Authorization": process.env.VUE_APP_AUTHORIZATION,
        'Cache-Control': 'no-cache'
    },
    adapter: throttleAdapterEnhancer(axios.defaults.adapter, throttleConfig)
});

export default httpClient;