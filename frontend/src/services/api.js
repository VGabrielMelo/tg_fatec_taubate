
import Axios from 'axios';
const API_BASE_URL = process.env.API_BASE_URL || 'http://localhost:5000' || 'http://l127.0.0.1:5000' ;
const api = Axios.create({
    baseURL:API_BASE_URL
})

api.interceptors.response.use(function (response) {
    if(response.status===403){
        response.data = {errors:[]}
        response.data.errors.push("Sessão expirada. Faça login novamente.")
    } 
    return response
  });

export default api;