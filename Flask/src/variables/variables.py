import os

class Variables():
    def __init__(self):
        self.db_uri = "SMARTFEELINGS_DATABASE_URI" in os.environ and os.environ['SMARTFEELINGS_DATABASE_URI'] or  "postgresql://rnsibxkn:glTdKMCJR9PMpTrmlEtrpMJW2StbFzBc@tuffi.db.elephantsql.com/rnsibxkn"
        self.jwt_secret = "SMARTFEELINGS_JWT_SECRET" in os.environ and os.environ['SMARTFEELINGS_JWT_SECRET'] or "smartfeelings-123"
        self.host = "FLASK_RUN_HOST" in os.environ and os.environ['FLASK_RUN_HOST'] or "0.0.0.0"
        self.port = "FLASK_RUN_PORT" in os.environ and os.environ['FLASK_RUN_PORT'] or "5000"       
        self.twitter_bearer_token="TWITTER_BEARER_TOKEN" in os.environ and os.environ['TWITTER_BEARER_TOKEN'] or "AAAAAAAAAAAAAAAAAAAAANn1awEAAAAAiZEjSkESGs7LdD8Jc0jaJxPMPmo%3DYQtmaiyfhgtuQHsphthoyfvGlMjXp4orBRx1oMX0sRYl50paOz" 
        self.page2api_api_key="PAGE2API_API_KEY" in os.environ and os.environ['PAGE2API_API_KEY'] or "2535b8f7f9691475991f9de139c0453615fd4a3e"
        self.caminhoNlp = "src/services/reviews_merge.json"
variables = Variables()