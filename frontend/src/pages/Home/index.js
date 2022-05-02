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
      <>

        <section id="navBarSection">
          <Row id="row-header">
            <Header />
          </Row>
        </section>

        <section id="bannerSection">
          <Container>
              <Row className="row-texto">
                <Col md={12}>
                  <h1 as={Col} className="titleHome">Plataforma para melhores <br></br> experiências entre marcas e consumidores. </h1>
                </Col>
                <Col md={12}>
                  <Form className="form-empresa" onSubmit={submitEmpresa}>
                      <InputGroup className="searchInput">
                          <Form.Control
                              className="mb-2"
                              id="nome-empresa"
                              placeholder="Pesquise aqui o nome da empresa"
                          />
                          <Button className="btn mb-2 btn-submit-form-empresa" type="submit"><FaSearch /></Button>
                      </InputGroup>
                  </Form>
                </Col>
              </Row>
          </Container>
        </section>

        <section id="processingSection">
          <Container>
            <Row className="row-texto" id="linguagem-natural">
                  <Col md={12}>
                    <h2 as={Col} className="titleHome">Processamento de Linguagem Natural.</h2>
                    <p as={Col} className="description">Officia aliquip qui duis eu enim anim consectetur. Adipisicing adipisicing enim labore esse aute aute sit ipsum cillum. Nisi labore duis ut nulla velit laboris sint laborum anim culpa in eu reprehenderit labore. Officia ex ut pariatur et non quis in. Sunt eu labore velit magna exercitation mollit ea culpa aliqua consequat ad cillum aliqua aute. Pariatur non aliqua ad Lorem duis magna eu sit incididunt.</p>
                  </Col>
              </Row>
          </Container>
        </section>

        <section id="aplicationsSection">
          <Container>
            <Row>

              <Col md={12}>
                <div className="titleHolder" id="aplicacoes">
                  <h2 as={Col} className="titleHome">Aplicações</h2>
                  <p as={Col} className="description">Sint aliquip veniam duis veniam aliqua quis.</p>
                </div>
              </Col>
              
              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE CRISES E REPUTAÇÃO</h3>
                    <p className="description">Ullamco ex commodo deserunt irure. Velit qui in consequat tempor adipisicing labore pariatur voluptate reprehenderit eiusmod duis. Nostrud nulla laborum non ad mollit laboris ut reprehenderit culpa minim amet laborum. Nostrud nostrud nulla dolore et proident fugiat labore mollit nulla dolore.</p>
                </div>
              </Col>

              <Col md={6} >
                  <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE CAMPANHAS E MARKETING</h3>
                    <p className="description">Cupidatat ipsum duis cillum veniam ea duis. Tempor est ut id nisi esse aliqua. Proident aute laborum labore anim do sit enim adipisicing cupidatat et dolor. Dolore ullamco ut minim sint excepteur exercitation dolore dolore. Ex quis officia laboris consequat.</p>
                  </div>
              </Col>

              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">MEDIÇÃO DE CRISES</h3>
                    <p className="description">Id dolore aute anim nulla. Laboris irure excepteur in irure. Aliquip esse tempor non et magna labore consequat eu mollit enim anim amet aliquip adipisicing.</p>
                </div>
              </Col>

              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE COMUNIDADE </h3>
                    <p className="description" >Adipisicing qui fugiat laborum culpa nulla reprehenderit. Culpa pariatur aliqua consequat officia. Amet in proident eiusmod reprehenderit dolor consequat commodo cupidatat et qui aute aliqua.</p>
                </div>
              </Col>

            </Row>
          </Container>
        </section>

      </>
    );
}

export default Home;
