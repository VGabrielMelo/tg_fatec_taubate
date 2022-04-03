import os

class Variables():
    def __init__(self):
        self.db_uri = "SMARTFEELINGS_DATABASE_URI" in os.environ and os.environ['SMARTFEELINGS_DATABASE_URI'] or  "postgresql://rnsibxkn:glTdKMCJR9PMpTrmlEtrpMJW2StbFzBc@tuffi.db.elephantsql.com/rnsibxkn"
        self.jwt_secret = "SMARTFEELINGS_JWT_SECRET" in os.environ and os.environ['SMARTFEELINGS_JWT_SECRET'] or "smartfeelings-123"
        self.host = "FLASK_RUN_HOST" in os.environ and os.environ['FLASK_RUN_HOST'] or "0.0.0.0"
        self.port = "FLASK_RUN_PORT" in os.environ and os.environ['FLASK_RUN_PORT'] or "5000"        
variables = Variables()