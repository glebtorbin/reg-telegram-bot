from datetime import date

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import (
    Column, ForeignKey, BigInteger, Text, Date, Integer, String, create_engine, PrimaryKeyConstraint
)

# Question
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fio = Column(Text)
    datar = Column(Date)
    id_role = Column(Integer, ForeignKey('roles.id'))

    # def __init__(self, id: BigInteger, fio: Text, datar: Date, id_role: Integer) -> None:
    #     self.id = id
    #     self.fio = fio
    #     self.datar = datar
    #     self.id_role = id_role

    def __repr__(self) -> str:
        return f'{self.fio}, {self.id}, {self.datar}, {self.id_role}'


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user = relationship('User')

    # def __repr__(self) -> str:
    #     return f'{self.id}, {self.name}'

users = [
    User(fio='Торбин Глен Андреевич', datar=date(2000, 5, 30), id_role=4),
    User(fio='Климешина Маша', datar=date(1999, 6, 3), id_role=2)
]

roles = [Role(name='дворник'), Role(name='грузчик')]

session_maker = sessionmaker(bind=create_engine('sqlite:///sqlite.db'))

def create_users():
    with session_maker() as session:
        for user in users:
            session.add(user)
        session.commit()

def create_role():
    with session_maker() as session:
        for role in roles:
            session.add(role)
        session.commit()



for i in session_maker().query(User).all():
    print(i)