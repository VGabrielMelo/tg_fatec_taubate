import React from 'react';
import { Container, Col, Nav, Navbar, Row } from "react-bootstrap";
import { FaSignOutAlt } from 'react-icons/fa'
import logo from './../../images/logo.png'
import Usuario from '../../js/Usuario';
import "./index.css"

const Header = (props) => {
    let token = localStorage.getItem("token")
    const logoutUsuario = () => {
        try {
            Usuario.logout()
            window.location.href = "/"
        } catch (error) {
            console.log(error);
        }
    }
    return (
      <>
        <Navbar expand="lg">
            <Container >
                <Col xs={2}>
                    <Nav.Link href="/">
                        <img
                            alt="Logo"
                            src={logo}
                            width="150em"
                            className="d-inline-block align-top"
                        />
                    </Nav.Link>
                </Col>

                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">

                <Col xs={10}>
                    <Nav fill justify className="me-auto" >
                        <Nav.Item>
                            <Nav.Link href="">Sobre</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link href="/#linguagem-natural">Linguagem Natural</Nav.Link>
                        </Nav.Item>
                        <Nav.Item>
                            <Nav.Link href="/#aplicacoes">Aplicações</Nav.Link>
                        </Nav.Item>
                        {token 
                            ?
                                <Nav.Item>
                                    <Nav.Link href="/perfil">Perfil</Nav.Link>
                                </Nav.Item>
                            :
                                <></>
                        }
                        <Nav.Item className="menuButtom">
                            {token 
                                ?
                                    <Nav.Link onClick={logoutUsuario} className="btn"><FaSignOutAlt /></Nav.Link>
                                :
                                    <Nav.Link href="/auth" className="btn">Login</Nav.Link>
                            }
                        </Nav.Item>
                    </Nav>
                </Col>
                </Navbar.Collapse>
            </Container>
        </Navbar>
     </>
    );
}

export default Header
