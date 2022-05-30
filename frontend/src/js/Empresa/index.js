import api from "./../../services/api";

const search = async (nome_empresa) => {
    let token = localStorage.getItem("token")
    let config = {
        headers: {
            'Authorization':`Bearer ${token}`
        }
    }
    let response = await api.get(`/empresas/${nome_empresa}/`,config)
    return response
}

// eslint-disable-next-line import/no-anonymous-default-export
export default {
    search: search
 };
