# -*- coding:utf-8 -*-

from flask import Flask
from {{cookiecutter.package_name}}.config import Config

import {{cookiecutter.package_name}}.models
# 初始化数据库表的注册

app = Flask(__name__)

# config
app.config.from_object(Config)

# app router
with app.app_context():
    from .views import user_view
    app.register_blueprint(user_view, url_prefix="/user")
