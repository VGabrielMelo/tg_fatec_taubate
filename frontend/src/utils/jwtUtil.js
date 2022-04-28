import jwt from 'jsonwebtoken';

const JWT_SECRET = process.env.SMARTFEELINGS_JWT_SECRET || 'smartfeelings-123';

let validToken = (token) => {
    try {
        jwt.verify(token, JWT_SECRET);
        return true
    } catch(err) {
        return false
    }
}

export default validToken;

