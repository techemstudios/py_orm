
from db.setup import *

class ApiBase():
    id = Column(Integer, primary_key=True)

    @classmethod
    def get(cls,id):
        session = Session()
        return session.query(cls).get(id)
        
    @classmethod
    def post(cls,instance_data):
        session = Session()
        instance = cls(**instance_data)
        session.add(instance)
        session.commit()
        return instance
        
    @classmethod
    def delete(cls,id):
        session = Session()
        instance = session.query(cls).get(id)
        session.delete(instance)
        session.commit()
        return None
        
    @classmethod
    def put(cls,id,instance_data):
        session = Session()
        instance = session.query(cls).get(id)
        for key,value in instance_data.items():
            setattr(instance,key,value)
        session.commit()
        return instance

    @classmethod
    def all(cls):
        session = Session()
        print("Just got session.")
        return session.query(cls).order_by(cls.id).all()
