from db.setup import *
from flask_restful import Resource, fields, marshal

from models.site import *
from models.stream import *

class Admin(Resource):
    
    def get(self):
        Base.metadata.create_all(bind=engine)

        # check table exists
        ins = inspect(engine)
        return ins.get_table_names(),200
