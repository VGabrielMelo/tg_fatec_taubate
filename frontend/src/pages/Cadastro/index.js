import { React, useState } from "react";

import { Container, Row, Col,Form, InputGroup, FormControl, Button, Nav } from "react-bootstrap";
import Header from "../../components/Header";
import Usuario from "../../js/Usuario";
import $ from 'jquery';
import "./index.css";

function Cadastro() {
    const cadastroUsuario = async (e) => {
        e.preventDefault()
        let response
        let usuario = {
            "nome":$("#nome-usuario").val(),
            "email":$("#email-usuario").val(),
            "senha":$("#senha-usuario").val()
        }
        try {
            response = await Usuario.cadastro(usuario)
            window.location.href = "/auth"
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
                <Form className="justify-content-center form-cadastro" onSubmit = {cadastroUsuario}>
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
                            <Form.Label htmlFor="nome-usuario" visuallyHidden>Nome</Form.Label>
                            <Form.Control
                                className="mb-2"
                                id="nome-usuario"
                                placeholder="Digite seu nome"
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
                                <Button id="btn btn-submit-cadastro-form " type="submit">Cadastro</Button><br/>
                            </div>
                        </Col>
                    </Row>
                </Form>
            </Row>
            
        </Container>
    );
}

export default Cadastro;
