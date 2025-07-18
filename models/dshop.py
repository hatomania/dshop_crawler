from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dshop(Base):
    __tablename__ = "dshops"

    id = Column(Integer, primary_key=True, autoincrement=True)
    index = Column(Integer, nullable=False)
    url = Column(String(512), nullable=False)
    shop_name = Column(String(255), nullable=False)
    reception_time = Column(String(255), nullable=False)
    holidays = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    delivery_person = Column(String(255), nullable=False)
    note = Column(Text, nullable=True) # これだけnullable OK
