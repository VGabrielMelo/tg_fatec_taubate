import { React, useEffect, useState } from "react"
import { Container, Row, Col } from "react-bootstrap"
import { useParams } from "react-router-dom"
import { Doughnut } from "react-chartjs-2"
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';
import $ from 'jquery';

import Empresa from "./../../js/Empresa";
import Header from "../../components/Header"
import mediumFace from "./../../images/medium-face.png"
import angryFace from "./../../images/angry-face.png"
import happyFace from "./../../images/happy-face.png"
import "./index.css";

function Results() {
    ChartJS.register(ArcElement, Tooltip, Legend);
    const { nome_empresa } = useParams();
    const [comentarios, setComentarios] = useState({})
    const [dataChart, setDataChart] = useState({})
    const chartOptions = {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Porcentagem de comentários negativos, positivos e neutros da empresa'
            }
        }
    }
    const searchEmpresa = async (nome_empresa) => {
        let response = await Empresa.search(nome_empresa)
        if (response.status === 200) {
            let data = response.data
            let nps = parseFloat(data.porcentagem_positivo)-parseFloat(data.porcentagem_negativo)
            if (nps >= 75) {
                $("#goodResult").removeClass("desactiveResult")
                $("#goodResult").addClass("activeResult")
            }
            if (nps < 75 && nps >= 50) {
                $("#goodResult").removeClass("desactiveResult")
                $("#goodResult").addClass("activeResult")
            }
            if (nps < 50 && nps >= 0) {
                $("#neutralResult").removeClass("desactiveResult")
                $("#neutralResult").addClass("activeResult")
            }
            if (nps < 0) {
                $("#badResult").removeClass("desactiveResult")
                $("#badResult").addClass("activeResult")
            }
            setComentarios({
                top_positivos: data.top_positivos,
                top_negativos: data.top_negativos
            })
            setDataChart({
                labels: ["Positivos", "Negativos", "Neutros"],
                datasets: [
                    {
                        label: "% de comentários negativos,positivos e neutros da empresa",
                        data: [
                            data.porcentagem_positivo,
                            data.porcentagem_negativo,
                            data.porcentagem_neutro,
                        ],
                        backgroundColor: ["#50AF95", "#d40000", "#ecf0f1"]
                    }
                ]
            })
        }
    }

    useEffect(() => {
        searchEmpresa(nome_empresa);
    }, []);

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
                            <h1 as={Col} className="titleResults">Plataforma para melhores <br></br> experiências entre marcas e consumidores.</h1>
                        </Col>
                    </Row>
                </Container>
            </section>

            <section id="resulSection">
                <Container>
                    <Row className="row-texto">
                        <Col md={12}>
                            <h2 as={Col} className="titleResults">
                                Resultado:
                            </h2>
                            <div className="holderResults">
                                <div className="desactiveResult" id="badResult">
                                    <img src={angryFace} alt="rosto bravo" className="" />
                                    <p className="description">Ruim</p>
                                </div>

                                <div className="desactiveResult" id="neutralResult">
                                    <img src={mediumFace} alt="rosto ok" className="" />
                                    <p className="description">Regular</p>
                                </div>

                                <div className="desactiveResult" id="goodResult">
                                    <img src={happyFace} alt="rosto feliz" className="" />
                                    <p className="description">Bom</p>
                                </div>
                            </div>
                        </Col>
                    </Row>
                </Container>
            </section>
            {/* <section id="resumeSection">
                <Container>
                    <Row className="row-texto">
                        <Col md={12}>
                            <h2 as={Col} className="titleResults">
                                Resumo da Empresa:
                            </h2>
                            <p className="description">
                                Lorem Ipsum is simply dummy text of the printing and typesetting
                                industry. Lorem Ipsum has been the industry's standard dummy
                                text ever since the 1500s, when an unknown printer took a galley
                                of type and scrambled it to make a type specimen book. It has
                                survived not only five centuries, but also the leap into
                                electronic typesetting, remaining essentially unchanged. It was
                                popularised in the 1960s with the release of Letraset sheets
                                containing Lorem Ipsum passages, and more recently with desktop
                                publishing software like Aldus PageMaker including versions of
                                Lorem Ipsum.
                            </p>
                        </Col>
                    </Row>
                </Container>
            </section> */}
            {Object.keys(dataChart).length !== 0 &&
                <section id="chartSection">
                    <Container>
                        <Row className="row-texto">
                            <Col md={12}>
                                <h2 as={Col} className="titleResults">Classificação de comentários da empresa: </h2>
                                <div id="chartDiv" >
                                    <Doughnut data={dataChart} options={chartOptions} />
                                </div>
                            </Col>
                        </Row>
                    </Container>
                </section>
            }
            {Object.keys(dataChart).length !== 0 &&
                <section id="commentSection">
                    <Container>
                        <Row className="row-texto">
                            <Col md={12}>
                                <h2 as={Col} className="titleResults">Top 10 comentários positivos :</h2>
                                {comentarios.top_positivos.map((value, index) => {
                                    return <p className="description" key={index}>{value}</p>;
                                })}
                            </Col>
                        </Row>
                        <Row className="row-texto">
                            <Col md={12}>
                                <h2 as={Col} className="titleResults">Top 10 comentários negativos :</h2>
                                {comentarios.top_negativos.map((value, index) => {
                                    return <p className="description" key={index}>{value}</p>;
                                })}
                            </Col>
                        </Row>

                    </Container>
                </section>
            }
        </>
    );
}

export default Results;
