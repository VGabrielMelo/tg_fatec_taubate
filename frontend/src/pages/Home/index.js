import { React, useState } from "react";
import { Container, Row, Col, Form, InputGroup, Button, Card } from "react-bootstrap";

import Header from "../../components/Header";
import { FaSearch } from "react-icons/fa";
import $ from "jquery"
import "./index.css";

function Home() {
    let submitEmpresa = async (e) => {
        e.preventDefault()
        let nome_empresa = $("#nome-empresa").val()
        window.location.href = `/resultado/${nome_empresa}`
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
                    <p as={Col} className="description">
                    O processamento de linguagem natural (PLN) usa machine learning para revelar a estrutura e o significado do texto, possibilitando que uma máquina possa compreender automaticamente frases escritas ou faladas por humanos.
                    </p>
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
                  <p as={Col} className="description"></p>
                </div>
              </Col>
              
              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE CRISES E REPUTAÇÃO</h3>
                    <p className="description">Possibilita a redução de prejuízos durante uma crise, preparando a liderança para tomar decisões.</p>
                </div>
              </Col>

              <Col md={6} >
                  <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE CAMPANHAS E MARKETING</h3>
                    <p className="description">Permite que a equipe de marketinf foque nos pontos forte quando for realizar alguma campanha.</p>
                  </div>
              </Col>

              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">MEDIÇÃO DE CRISES</h3>
                    <p className="description">Colabora para a análise dos dados no caso de uma crise.</p>
                </div>
              </Col>

              <Col md={6} className="">
                <div className="aplicationHolder">
                    <h3 className="titleAplication">GESTÃO DE COMUNIDADE </h3>
                    <p className="description" >Cria uma interação entre você, seus clientes e seus colaboradores, podendo analisar a opinião e satisfação deles.</p>
                </div>
              </Col>

            </Row>
          </Container>
        </section>
        <section id="classificationSection">
          <Container>
            <Row className="row-texto" id="classificacao">
                  <Col md={12}>
                    <h2 as={Col} className="titleHome">Classificação</h2>
                    <p as={Col} className="description">
                    Utilizamos o rank NPS (Net Promoter Score) para realizar a classificação dos comentários das empresas, seguindo o padrão abaixo:
                    
                    </p>
                    <Card body>Ruim: índices entre 0% e 69%</Card>
                    <Card body>Regular: índices entre 70% e 89%</Card>
                    <Card body>Bom: índices entre 90% e 100%</Card>
                  </Col>
              </Row>
          </Container>
        </section>

      </>
    );
}

export default Home;
