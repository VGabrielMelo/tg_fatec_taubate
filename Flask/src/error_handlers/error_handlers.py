""" from src.server.instance import server

app = server.app

def handle_bad_request(message):
    return message, 400

def handle_unauthorized(message):
    return message, 401

app.register_error_handler(400, handle_bad_request)
app.register_error_handler(401, handle_unauthorized)
 """