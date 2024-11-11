from database import Base

from sqlalchemy import TIMESTAMP, Column, ForeignKey, \
                        Integer, LargeBinary, SmallInteger, String


# Описание сущности users
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    login = Column(String)
    passwd = Column(String)
    secret = Column(String)
    photo = Column(LargeBinary)
    key_crypt = Column(LargeBinary)
    initial_passwd = Column(SmallInteger)


# Описание сущности repository
class Repository(Base):
    __tablename__ = 'repository'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service = Column(String)
    login = Column(String)
    passwd = Column(String)
    description = Column(String)
    initial_log = Column(SmallInteger)
    initial_passwd = Column(SmallInteger)


class Ban(Base):
    __tablename__ = 'ban'

    id = Column(Integer, primary_key=True)
    count = Column(Integer)
    email = Column(String, ForeignKey('users.id'))
    time = Column(TIMESTAMP)