import React from 'react';
import {Routes, BrowserRouter, Route, Navigate } from 'react-router-dom';

import isAuth from './utils/isAuth';
import Home from './pages/Home'
import NotFound from './pages/NotFound'
import Login from './pages/Login'
import Cadastro from './pages/Cadastro'
import Resultado from './pages/Resultado'


function Rotas(){
    
    /* const PrivateRoute = ({component: Component, ...rest})=>(
        <Route {...rest} render ={props =>(
            isAuth()?(
                <Component {...props}/>
            ):(
                <Navigate to ={{pathname:'/',state:{from: props.location}}}/>
            )
        )}/>
    ) */
    /* const PublicRoute = ({component: Component, ...rest})=>(
        <Route {...rest} render ={props =>(
            isAuth()?(
                <Navigate to ={{pathname:"/",state:{from: props.location}}}/>
            ):(
                <Component {...props}/>
            )
        )}/>
    ) */

    const PrivateRoute = ({ children }) => {
        return isAuth() ? children : <Navigate to="/" />;
    }       
    
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/auth" element={<Login/>} />
                <Route path="/cadastro" element={<Cadastro/>} />
                <Route path="/resultado/:nome_empresa" element={<Resultado/>} />
                <Route path="/*" element={<NotFound/>} />
                <Route path="/*" element={<PrivateRoute><NotFound /></PrivateRoute>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default Rotas;