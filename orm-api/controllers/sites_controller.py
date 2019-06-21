from resources.site_resource import *

def site_add(api):
    api.add_resource(SiteList,'/api/sites')
    # List sites for stream
    api.add_resource(SitesOnStream,'/api/streams/<id>/sites')

    api.add_resource(SiteResource,'/api/sites/<id>')


    
