# coding=utf-8
from uuid import uuid4
from datetime import datetime
from string import printable

from sqlalchemy import (create_engine, Column, Integer, String,
                        Text, Boolean, Date, DateTime, ForeignKey)

from {{cookiecutter.package_name}}.repositorys.dbsession import Base


class user_model(Base):
    __tablename__ = 'user1'
    uuid = Column(String(36), unique=True, nullable=False,
                  default=lambda: str(uuid4()))
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), nullable=False)
    _password = Column('password', String(64))
    createtime = Column(DateTime, default=datetime.now)
    update_time = Column(DateTime)
    last_login = Column(DateTime)
    loginnum = Column(Integer, default=0)
    _locked = Column(Boolean, default=False, nullable=False)

    _avatar = Column(String(64))

    def to_dict(self):
        return {
            "id": self.id,
            "userName": self.user_name
        }
