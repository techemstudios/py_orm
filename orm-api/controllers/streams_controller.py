from resources.stream_resource import *

def stream_add(api):
    api.add_resource(StreamList,'/api/streams')
    api.add_resource(StreamResource,'/api/streams/<id>')
