from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dshop(Base):
    __tablename__ = "dshops"

    id = Column(Integer, primary_key=True, autoincrement=True)
    index = Column(Integer, nullable=False, unique=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    url = Column(String(512), nullable=False)
    status = Column(Integer, nullable=False)
    responsed_code = Column(Integer, nullable=False)
    etag = Column(String(255), nullable=True)
    shop_name = Column(String(255), nullable=True)
    reception_time = Column(String(255), nullable=True)
    holidays = Column(String(255), nullable=True)
    address = Column(String(255), nullable=True)
    delivery_person = Column(String(255), nullable=True)
    note = Column(Text, nullable=True)
