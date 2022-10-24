from flask import Blueprint
from datetime import datetime, timedelta

time=Blueprint('time', __name__)

@time.route("/musedash/v1/time", methods=['GET'])
def time_game():
    data={
        "code": 0,
        "data": {
            "server_time": int(round(datetime.utcnow().timestamp()))
        }
    }
    return data, 200 , {'Content-Type': 'application/json'}

