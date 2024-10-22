from sqlalchemy import MetaData
from sqlalchemy import Column, Boolean, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase
import datetime

metadata = MetaData()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)

    name = Column(String(50), unique=False, nullable=False)
    surname = Column(String(50), unique=False, nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(256), unique=True, nullable=False)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=False, nullable=False)

    title = Column(String(100), unique=False, nullable=False)
    content = Column(String(1000), unique=False, nullable=False)
    mediaLinks = Column(String(1000))
    tags = Column(String(1000))

    likes = Column(Integer, unique=False, nullable=True)
    shares = Column(Integer, unique=False, nullable=True)
    isFavorite = Column(Boolean, default=False)

    createdAt = Column(DateTime, default=datetime.datetime.utcnow)

class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, unique=False, nullable=False)

    content = Column(String(1000), unique=False, nullable=False)

    createdAt = Column(DateTime, default=datetime.datetime.utcnow)