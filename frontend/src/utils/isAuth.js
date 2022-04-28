import validToken from './jwtUtil'

const isAuth = () =>{
    let token = localStorage.getItem("token")
    if(token && validToken(token)){
        return true
    } else {
        localStorage.removeItem("token")
        localStorage.removeItem("manterConectado")
        return false
    }
}
export default isAuth;