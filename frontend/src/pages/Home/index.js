import { React, useState } from "react";

import { Container, Row, Col, Form, InputGroup, Button } from "react-bootstrap";
import Header from "../../components/Header";
import getEmpresaByName from "../../js/Empresa";
import { FaSearch } from "react-icons/fa";
import $ from "jquery"
import "./index.css";

function Home() {
    const submitEmpresa = async (e) => {
        e.preventDefault()
        let nome_empresa = $("#nome-empresa").val()
        let response
        try {
            response = await getEmpresaByName(nome_empresa)
        } catch (error) {
            console.log(error.response);
        } 
        console.log(response);
    }
    return (
        <Container id="home" fluid>
            <Row id="row-header">
                <Header />
            </Row>
            <Row className="row-texto">
                <Row className="justify-content-center">
                    <span as={Col} className="titulo-home ">Plataforma para melhores experiências entre marcas e consumidores.</span>
                </Row>
                <Form className="justify-content-center form-empresa" onSubmit={submitEmpresa}>
                    <Row className="align-items-center justify-content-center">
                        <Col xs={7}>
                            <InputGroup >
                                <Form.Control
                                    className="mb-2"
                                    id="nome-empresa"
                                    placeholder="Pesquise aqui o nome da empresa"
                                />
                                <Button className="btn mb-2 btn-submit-form-empresa" type="submit"><FaSearch /></Button>
                            </InputGroup>

                        </Col>
                    </Row>
                </Form>
            </Row>
            <Row className="row-texto" id="linguagem-natural">
                <Row className="justify-content-center">
                    <span as={Col} className="titulo-home">Processamento de Linguagem Natural.</span><br /><br /><br />
                    <span as={Col} className="texto-home texto-processamento">Officia aliquip qui duis eu enim anim consectetur. Adipisicing adipisicing enim labore esse aute aute sit ipsum cillum. Nisi labore duis ut nulla velit laboris sint laborum anim culpa in eu reprehenderit labore. Officia ex ut pariatur et non quis in. Sunt eu labore velit magna exercitation mollit ea culpa aliqua consequat ad cillum aliqua aute. Pariatur non aliqua ad Lorem duis magna eu sit incididunt.</span>
                </Row>
            </Row>
            <Row id="aplicacoes">
                <Row className="justify-content-center">
                    <span as={Col} className="titulo-home ">Aplicações</span>
                    <span as={Col} className="texto-home" style={{ textAlign: "center", margin: "2rem auto 4rem auto" }}>Sint aliquip veniam duis veniam aliqua quis.</span>
                    <Row className="texto-home justify-content-center">
                        <Col xs={5} className="texto-home div-texto-aplicacoes">
                            <div as={Col} className="titulo-home titulo-aplicacoes">GESTÃO DE CRISES E REPUTAÇÃO</div>
                            <div className="texto-aplicacoes">Ullamco ex commodo deserunt irure. Velit qui in consequat tempor adipisicing labore pariatur voluptate reprehenderit eiusmod duis. Nostrud nulla laborum non ad mollit laboris ut reprehenderit culpa minim amet laborum. Nostrud nostrud nulla dolore et proident fugiat labore mollit nulla dolore.</div>
                        </Col>
                        <Col xs={{ span: 5, offset: 2 }} className="texto-home div-texto-aplicacoes">
                            <div as={Col} className="titulo-home titulo-aplicacoes">GESTÃO DE CAMPANHAS E MARKETING</div>
                            <div className="texto-aplicacoes">Cupidatat ipsum duis cillum veniam ea duis. Tempor est ut id nisi esse aliqua. Proident aute laborum labore anim do sit enim adipisicing cupidatat et dolor. Dolore ullamco ut minim sint excepteur exercitation dolore dolore. Ex quis officia laboris consequat.</div>
                        </Col>
                    </Row>
                    <Row className="texto-home justify-content-center">
                        <Col xs={5} className="texto-home div-texto-aplicacoes">
                            <div as={Col} className="titulo-home titulo-aplicacoes">MEDIÇÃO DE CRISES</div>
                            <div className="texto-aplicacoes">Id dolore aute anim nulla. Laboris irure excepteur in irure. Aliquip esse tempor non et magna labore consequat eu mollit enim anim amet aliquip adipisicing.</div>
                        </Col>
                        <Col xs={{ span: 5, offset: 2 }} className="texto-home div-texto-aplicacoes">
                            <div as={Col} className="titulo-home titulo-aplicacoes">GESTÃO DE COMUNIDADE</div>
                            <div className="texto-aplicacoes">Adipisicing qui fugiat laborum culpa nulla reprehenderit. Culpa pariatur aliqua consequat officia. Amet in proident eiusmod reprehenderit dolor consequat commodo cupidatat et qui aute aliqua.</div>
                        </Col>
                    </Row>
                </Row>
            </Row>
        </Container>
    );
}

export default Home;
