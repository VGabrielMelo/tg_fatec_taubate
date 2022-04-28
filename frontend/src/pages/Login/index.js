import { React, useState } from "react";
import { Container, Row, Col,Form, InputGroup, FormControl, Button,Nav } from "react-bootstrap";
import Header from "../../components/Header";
import Usuario from "../../js/Usuario";
import $ from 'jquery';

import "./index.css";

function Login() {
    const loginUsuario = async (e) => {
        e.preventDefault()
        let response
        let usuario = {
            "email":$("#email-usuario").val(),
            "senha":$("#senha-usuario").val()
        }
        try {
            response = await Usuario.auth(usuario)
            let token = response.data.token
            localStorage.setItem("token",token)
            window.location.href = "/"
        } catch (error) {
            console.log(error.response);
        }

    };
    return (
        <Container id="home" fluid>
            <Row id="row-header">
                <Header />
            </Row>
            <Row className="row-texto">
                <Row  className="justify-content-center">
                    <span as={Col} className="titulo-home ">Plataforma para melhores experiências entre marcas e consumidores.</span>
                </Row>
                <Form className="justify-content-center form-login" onSubmit={loginUsuario}>
                    <Row className="align-items-center justify-content-center">
                        <Col xs={6}>
                            <Form.Label htmlFor="email-usuario" visuallyHidden>Email</Form.Label>
                            <Form.Control
                                type="email" 
                                className="mb-2"
                                id="email-usuario"
                                placeholder="Digite seu email"
                                required
                            />
                            <Form.Label htmlFor="senha-usuario" visuallyHidden>Senha</Form.Label>
                            <Form.Control
                                type="password" 
                                className="mb-2"
                                id="senha-usuario"
                                placeholder="Digite sua senha"
                                required
                            />
                            <div className="d-grid gap-2">
                                <Button id="btn-submit-login-form btn" type="submit">Login</Button><br/>
                            </div>
                        </Col>
                        <center>
                            <span as={Col} className="texto-home" style={{fontSize:"1.2rem"}}><Nav.Link href="/cadastro">Não tem cadastro? <span>Cadastre-se</span></Nav.Link></span>
                        </center>
                    </Row>
                </Form>
            </Row>
            
        </Container>
    );
}

export default Login;
