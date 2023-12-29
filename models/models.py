from sqlalchemy import Table, Column
from sqlalchemy import Integer, VARCHAR, TIMESTAMP
from sqlalchemy import ForeignKey

from .datebase import Base

from datetime import datetime


class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(50), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    users = Column(Integer, ForeignKey('users.id'), nullable=False)

    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(50), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
