# coding=utf-8
from {{cookiecutter.package_name}}.repositorys.dbsession import Base
from {{cookiecutter.package_name}}.repositorys.dbsessionn import engine
# 注册表
from {{cookiecutter.package_name}}.models.user import user_model

Base.metadata.create_all(engine)
