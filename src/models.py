import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

followers_table = Table('followers', Base.metadata,
    Column('from_id', Integer, ForeignKey('user.id')),  #foreignKey is inherited
    Column('to_id', Integer, ForeignKey('user.id'))
)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password = 'somehashedcode'
    followers = relationship(
        'User',
        secondary = followers_table,
        back_populates="Users")
    posts = relationship("Post")
    comments = relationship("Post")

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comments = relationship("Comments")

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')