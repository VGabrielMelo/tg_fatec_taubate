import { React } from "react";
import { Container, Row, Col, Form, InputGroup, Button } from "react-bootstrap";
import Header from "../../components/Header";
import mediumFace from './../../images/medium-face.png'
import angryFace from './../../images/angry-face.png'
import happyFace from './../../images/happy-face.png'
import "./index.css";


function Results() {
    return (
      <>
        <section id="navBarSection">
          <Row id="row-header">
            <Header />
          </Row>
        </section>

        <section id="titleSection">
          <Container>
              <Row className="row-texto">
                <Col md={12}>
                  <h1 as={Col} className="titleResults">Plataforma para melhores <br></br> experiências entre marcas e consumidores. </h1>
                </Col>
              </Row>
          </Container>
        </section>

        <section id="resulSection">
          <Container>
            <Row className="row-texto">
                  <Col md={12}>
                    <h2 as={Col} className="titleResults">Resultado:</h2>
                    <div className="holderResults">

                      <div className="desactiveResult">
                        <img src={angryFace} alt="rosto bravo"  className="" />
                        <p className="description">Ruim</p>
                      </div>

                      <div className="desactiveResult">
                        <img src={mediumFace} alt="rosto ok"    className="" />
                        <p className="description">Regular</p>
                      </div>

                      <div className="activeResult">
                        <img src={happyFace} alt="rosto felyz"  className="" />
                        <p className="description">Bom</p>
                      </div>
                     
                    </div>
                  </Col>
              </Row>
          </Container>
        </section>

        <section id="resumeSection">
          <Container>
            <Row className="row-texto">
                  <Col md={12}>
                    <h2 as={Col} className="titleResults">Resumo da Empresa:</h2>
                    <p className="description">
                      Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy 
                      text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
                      It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
                      It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and 
                      more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
                    </p>
                  </Col>
              </Row>
          </Container>
        </section>

        <section id="commentSection">
          <Container>
            <Row className="row-texto">
                  <Col md={12}>
                    <h2 as={Col} className="titleResults">Top 10 comentários : </h2>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                     <p className="description">Lorem impsum is simply</p>
                  </Col>
              </Row>
          </Container>
        </section>


      </>
    );
}

export default Results;
