# Get Database URI from appsettings

import os,json

#settings_file = os.path.join(app.instance_path, 'db', 'appsettings.json.')

settings = json.loads(open('db/appsettings.json').read())

db_config = settings['db_config']
db_url = "mysql+pymysql://%s:%s@%s/%s" % (db_config['user'],
    db_config['password'],
    db_config['host'],
    db_config['database'])

from sqlalchemy import (
    create_engine,
    inspect,
    Column,
    ForeignKey,
    String,
    Integer,
    Numeric,
    DateTime )

from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database

# Create the database if it doesn't exist
engine = create_engine(db_url)
if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

# We do need to get a Session from the engine to which we are bound.
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)