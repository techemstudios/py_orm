from flask_restful import Resource, fields, marshal, request
from models.stream import *

stream_fields = {
    'id' : fields.Integer(),
    'name' : fields.String()
}

class StreamList(Resource):
	
    def get(self):
        print("About to call get_all.")
        return marshal(Stream.all(),stream_fields), 200
        
    def post(self):
        stream = request.get_json(force=True)
        return marshal(Stream.post(stream),stream_fields), 201
        
class StreamResource(Resource):
    
    def get(self,id):
        return marshal(Stream.get(id),stream_fields), 200
    
    def put(self,id):
        stream = request.get_json(force=True)
        return marshal(Stream.put(id,stream),stream_fields), 200
    
    def delete(self,id):
        Stream.delete(id)
        return '', 204
