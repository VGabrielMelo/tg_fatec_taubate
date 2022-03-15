from src.server.instance import server
from src.controllers.empresa import *
from src.controllers.usuario import *
from src.models.models import db
db.drop_all()
db.create_all()
server.run()
