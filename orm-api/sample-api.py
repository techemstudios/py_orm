from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

# import all your controllers here
from controllers.admin_controller import *
from controllers.sites_controller import *
from controllers.streams_controller import *

# Helpful for debugging your Apache config
print('adding endpoints')
admin_add(api)
site_add(api)
stream_add(api)
