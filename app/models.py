from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import (
    Column, ForeignKey, Text, Date, Integer, String, create_engine
)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(Text)
    datar = Column(Date)
    id_role = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self) -> str:
        return f'{self.fio}, {self.id}, {self.datar}, {self.id_role}'


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship('User')


session_maker = sessionmaker(bind=create_engine('sqlite:///sqlite.db'))
