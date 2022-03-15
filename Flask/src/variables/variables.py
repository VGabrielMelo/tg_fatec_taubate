import os
import string
import random
class Variables():
    def __init__(self):
        #self.db_uri = os.environ['SMARTFEELINGS_DATABASE_URI']
        #self.jwt_secret = os.environ['SMARTFEELINGS_JWT_SECRET']
        #self.jwt_secret = 'smartfeelings-123'
        self.jwt_secret = ''.join(random.choice(string.ascii_letters+string.digits+string.ascii_uppercase)for i in range(12))
        self.db_uri = 'postgresql://rnsibxkn:glTdKMCJR9PMpTrmlEtrpMJW2StbFzBc@tuffi.db.elephantsql.com/rnsibxkn'
        
variables = Variables()