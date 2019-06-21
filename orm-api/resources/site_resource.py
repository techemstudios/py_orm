from flask_restful import Resource, fields, marshal, request

from models.site import *
from models.stream import *

site_fields = {
    'id' : fields.Integer(),
    'site_name' : fields.String(attribute="name"),
    'stream_name' : fields.String(attribute="stream.name")
}

class SiteList(Resource):
	
    def get(self):
        print("About to call get_all.")
        return marshal(Site.all(),site_fields), 200
        
    def post(self):
        site = request.get_json(force=True)
        return marshal(Site.post(site),site_fields), 201

class SitesOnStream(Resource):

    def get(self,id):
        return marshal(Stream.get(id).sites,site_fields), 200

class SiteResource(Resource):
    
    def get(self,id):
        return marshal(Site.get(id),site_fields), 200
        
    def put(self,id):
        site = request.get_json(force=True)
        return marshal(Site.put(id,site),site_fields), 200
        
    def delete(self,id):
        Site.delete(id)
        return '', 204
    
    