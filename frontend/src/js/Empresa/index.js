import api from "./../../services/api";

const getEmpresaByName = async (nome_empresa) => {
    let token = localStorage.getItem("token")
    let config = {
        headers: {
            'Authorization':`Bearer ${token}`
        }
    }
    let response = await api.get(`/empresas/${nome_empresa}/`,config)
    return response
}

export default getEmpresaByName;