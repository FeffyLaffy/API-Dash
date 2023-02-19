from flask import Blueprint
import json

approved_version=Blueprint('aprroved_version', __name__)

data = {
    "code": 0,
    "data": True,
    "msg": "ok"
}


@approved_version.route("/musedash/v1/approved_version", methods=['GET'])
def server_approve():
    return data, 200 , {'Content-Type': 'application/json'}