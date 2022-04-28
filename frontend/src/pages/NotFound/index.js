import { React } from "react";

import { Container } from "react-bootstrap";
import Header from "../../components/Header";
import "./index.css";

function NotFound() {

    return (
        <Container id="bot-found" fluid>
            <Header />
            <h1>404</h1>
        </Container>
    );
}

export default NotFound;
