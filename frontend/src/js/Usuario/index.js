import api from "./../../services/api";

const auth = async (usuario) => {
    let data = {...usuario}
    let response = await api.post("/usuarios/auth/",data)
    return response
}
const cadastro = async (usuario) => {
    let data = {...usuario}
    let response = await api.post("/usuarios/",data)
    return response
}
const logout = () => {
    localStorage.removeItem("token")
    localStorage.removeItem("manterConectado")
}

// eslint-disable-next-line import/no-anonymous-default-export
export default {
    auth: auth,
    logout: logout,
    cadastro: cadastro
 };