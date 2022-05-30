import { React, useEffect, useState } from "react"
import { Container, Row, Col } from "react-bootstrap"
import { useParams } from "react-router-dom"
import { Pie } from "react-chartjs-2"
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
            /* utilizar isso quando nao for necessario utilizar a api (pra economizar requisições ). tirar de dentro do if acima todo o codigo abaixo para que funcione 
            let response = {}
            response.data = {
                porcentagem_negativo: 9.8,
                porcentagem_neutro: 3.92,
                porcentagem_positivo: 84.97,
                top_negativos: [
                    [0.9414922325894202, "só entra parentes"],
                    [
                        0.9499338025890085,
                        "Já foi uma boa empresa ,mas a cultura de amizade lá dentro e muito grande só sobe ou tem alimento se tem amizades e favorsinhos com gestores incovenie",
                    ],
                    [
                        0.9591349083853064,
                        "Empresa muito boa, organizada, forte em tecnologia, preocupada com desenvolvimento de pessoas.",
                    ],
                    [0.9790648495042602, "Empresa boa, com uma má gestão."],
                    [
                        0.9974730228182533,
                        "Dificil fazer uma avaliação, pois trabalhei na Embraer por 37 anos e concluindo que após este tempo não houve reconhecimento pelo trabalho que fiz.",
                    ],
                    [0.997616865620157, "Não tem perspectiva de de crescimento de carreia"],
                    [
                        0.9994777708346942,
                        "muitas pessoas: muitos problemas. Empresa seria: gestão dos problemas",
                    ],
                    [0.9995477671657758, "Empresa que não aplica seus próprios principios"],
                    [
                        0.9996318226793384,
                        "Não existe meritocracia e cultura do desperdício",
                    ],
                    [0.9998037736451973, "Não é tudo o que aparenta"],
                ],
                top_positivos: [
                    [
                        0.9993178211442808,
                        "Excelente empresa, recomendo a qualquer pessoa interessada",
                    ],
                    [0.9993202985119162, "Excelentes profissionais"],
                    [
                        0.9994075869593437,
                        "a empresa e boa tem um ótimo desempenho em trabalho em grupo",
                    ],
                    [
                        0.9994965733887246,
                        "Empresa agradável , excelente lugar para trabalhar.",
                    ],
                    [0.9997143489582615, "Empresa dinâmica e excelente para trabalhar"],
                    [0.999714772244994, "Ótimo excelente"],
                    [0.9997474325197185, "Excelente empresa pra trabalhar"],
                    [
                        0.9998315435772842,
                        "Empresa maravilhosa, ótimas qualidades dos colaboradores e desenvolvimento profissional.",
                    ],
                    [
                        0.9999689274159351,
                        "Excelente empresa para trabalhar com ótimo salário e benefícios, ambiente bem dinâmico e colaborativo",
                    ],
                    [0.9999774535371087, "Empresa agradável e excelente profissionais"]
                ]
            } */
            let data = response.data
            if (data.porcentagem_positivo >= 90) {
                $("#goodResult").removeClass("desactiveResult")
                $("#goodResult").addClass("activeResult")
            }
            if (data.porcentagem_positivo < 90 && data.porcentagem_positivo >= 70) {
                $("#neutralResult").removeClass("desactiveResult")
                $("#neutralResult").addClass("activeResult")
            }
            if (data.porcentagem_positivo < 70 && data.porcentagem_positivo >= 60) {
                $("#badResult").removeClass("desactiveResult")
                $("#badResult").addClass("activeResult")
            }
            let positivos = []
            let negativos = []
            data.top_positivos.forEach((c, index) => {
                positivos.push(c[1])
            })
            data.top_negativos.forEach((c, index) => {
                negativos.push(c[1])
            })
            /* activeResult */
            setComentarios({
                top_positivos: positivos,
                top_negativos: negativos
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
                                    <Pie data={dataChart} options={chartOptions} />
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
