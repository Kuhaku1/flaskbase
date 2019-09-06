# -*- coding:utf-8 -*-

from flask import Blueprint, request
from {{cookiecutter.package_name}}repositorys.props import auth, success, error, panic
from {{cookiecutter.package_name}}.types.user_schema import InfoSchema

user_view = Blueprint("user_view", __name__)


@user_view.route("/info", methods=["GET"])
@panic(InfoSchema)
def fresh_info(args):
    return success({
        "result": {
            "id": 1
        }
    })
    return error(reason="not found")
