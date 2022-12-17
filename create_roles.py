from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from app.models import Role


roles = [Role(name='дворник'), Role(name='грузчик')]

session_maker = sessionmaker(bind=create_engine('sqlite:///sqlite.db'))


def create_role():
    with session_maker() as session:
        for role in roles:
            session.add(role)
        session.commit()


if __name__ == '__main__':
    create_role()