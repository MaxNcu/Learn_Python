import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
sys.path.append('..')
from app import db
print db

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/meizi", max_overflow=5)


Base = declarative_base()



class Users(Base):


    __tablename__ = 'data_meizi'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    url = Column(String(100))
    show_img = Column(String(100))
    all_img = Column(String(2000))
    table_args__ = (
        UniqueConstraint('id', 'url', name='uix_id_name'),
        Index('ix_id_name', 'title'),
    )

Base.metadata.create_all(engine)