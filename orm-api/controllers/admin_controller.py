from resources.admin_resource import *

def admin_add(api):
    # Admin API to create your db if needed.
    api.add_resource(Admin,'/api/admin/create_db')