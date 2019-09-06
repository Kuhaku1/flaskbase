# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from {{cookiecutter.package_name}}.config import Config  # 不推荐下级掉上级
# 连接数据库的数据
import os
# DB_URI的格式：dialect（mysql/sqlite）+driver://username:password@host:port/database?charset=utf8

# engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)
# sessionmaker生成一个session类
Session = sessionmaker(bind=engine)
dbSession = Session()
Base = declarative_base(engine)
