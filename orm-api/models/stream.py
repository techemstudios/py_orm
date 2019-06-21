from db.setup import *
from models.api_base import ApiBase

class Stream(ApiBase,Base):
    __tablename__ = 'streams'
    name = Column(String(64))
    description = Column(String(255))
    sites = relationship("Site", back_populates="stream")
