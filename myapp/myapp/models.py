import sys
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), nullable=False)


engine = create_engine('postgresql://vagrant:vagrant@localhost/myapp_db')

Base.metadata.create_all(engine)
