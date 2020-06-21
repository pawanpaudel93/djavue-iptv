import axios from 'axios'

const httpClient = axios.create({
    baseUrl: process.env.VUE_APP_BASE_URL,
    timeout: 5000, // indicates, 1000ms ie. 1 second
});

export default httpClient;