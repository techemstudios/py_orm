from db.setup import *
from models.api_base import ApiBase

class Site(ApiBase,Base):
    __tablename__ = 'sites'
    name = Column(String(64))
    latitude = Numeric(3,3)
    longitude = Numeric(3,3)
    stream_id = Column(Integer, ForeignKey('streams.id'))
    stream = relationship("Stream", back_populates="sites")
