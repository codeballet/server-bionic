from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from myapp import app

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_name = Column(String(80), nullable=False)
    date = Column(DateTime, default=func.now())


engine = create_engine(app.config['DB_URI'])

Base.metadata.create_all(engine)
