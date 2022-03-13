import os
class Variables():
    def __init__(self):
        #self.db_uri = os.environ['SMARTFEELINGS_DATABASE_URI']
        #self.jwt_secret = os.environ['SMARTFEELINGS_JWT_SECRET']
        self.db_uri = 'postgresql://rnsibxkn:glTdKMCJR9PMpTrmlEtrpMJW2StbFzBc@tuffi.db.elephantsql.com/rnsibxkn'
        self.jwt_secret = 'c21hcnRmZWVsaW5ncy0xMjM=' #smartfeelings-123
        
variables = Variables()