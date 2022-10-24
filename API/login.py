#MIT License

#Copyright (c) 2022 Feffy

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


from flask import Blueprint, jsonify, request, Response, url_for, redirect, session
from authlib.integrations.flask_client import OAuth
import json
import requests
from API.mongoJobs import Data, FindData
from discord_oauth2 import DiscordAuth


login=Blueprint('login', __name__)

CLIENT_ID = 'CLIENT_DISCORD_ID'
CLIENT_SECRET = 'CLIENT_SECERT'
REDIRECT_URI = 'https://user-us.peropero.net/oauth/google/login'

discord_auth = DiscordAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI)

def jsonResponseFactory(data):
    '''Return a callable in top of Response'''
    def callable(response=None, *args, **kwargs):
        '''Return a response with JSON data from factory context'''
        return Response(json.dumps(data), *args, **kwargs)
    return callable

def info(access_token):
    headers={
        'Authorization' : f"Bearer {access_token}",
        'Content-Type': 'application/json'
    }
    ab=requests.get("https://discord.com/api/v10/users/@me", headers=headers)
    ab.raise_for_status()
    return ab.json()

@login.route("/api/v1/me/info", methods=['GET', 'POST'])
def infov1():
    data = {
  "code": 0,
  "msg": "ok",
  "data": {
    "id": "428604",
    "username": "",
    "ban": False,
    "phone": "",
    "email": "",
    "real_name_verify": False,
    "status": "",
    "xd_id": "",
    "tx_id": "114092120",
    "is_fresh_user": True,
    "client_info": "musedash",
    "is_overseas": False,
    "is_auth": True,
    "is_md_auth": False,
    "pass_word_init": False
  }
    }
    return data, 200, {'Content-Type': 'application/json'}

@login.route('/oauth/google/login1', methods=['GET'])
def login_google():
    if request.args.get("code") is None:
        login_url = discord_auth.login()
        return redirect(login_url)
    else:
        return {"code":request.args.get("code"),"msg":"ok","data":{"token":request.args.get("code")}}, 200, {'Content-Type': 'application/json'}
        
@login.route("/oauth/google/login", methods=['GET'])
def get_info_discord():
    tokens = discord_auth.get_tokens(request.args.get("code"))
    data=info(tokens["access_token"])
    name=data["username"]
    discriminator=data["discriminator"]
    id=data["id"]
    a=Data(id, request.remote_addr, f"{name}#{discriminator}")
    a.get_or_make_data()
    #return str(data), 200, {'Content-Type': 'application/json; charset=utf-8'}
    return redirect(f"https://us-musedash.peropero.net/oauth/google/login1?code={id}")


@login.route("/api/v1/o/google/googleGetToken", methods=['GET'])
def postit():
    if request.args.get("code") is None:
        return "something wrong"
    else:
        return {"code":0,"msg":"ok","data":{"token":request.args.get("code")}}, 200, {'Content-Type': 'application/json'}

from flask import jsonify

@login.route('/user/account-oversea-login', methods=['GET'])
def acc_oversea_login_GET():
    FindPlayer=FindData(request.args.get("id"), request.remote_addr)
    player=FindPlayer.get_data_find_by_id()
    data={ 
        "auth": player["user_id"],
        "code": 0,
        "fresh": False,
        "profile": {
            "object_id" : str(player["_id"]),
            "created_at": player["created_at"],
            "updated_at": player["updated_at"],
            "user_id": player["user_id"],
            "nickname": player["nickname"]      
            },
        "uid": str(player["_id"]) 
    }
    return jsonify(data), 200, {'Content-Type': 'application/json'}

@login.route('/user/account-oversea-login', methods=['POST'])
def acc_oversea_login_POST():
    FindPlayer=FindData(request.args.get("id"), request.remote_addr)
    player=FindPlayer.get_data_find_by_id()
    data={ 
        "auth": player["user_id"],
        "code": 0,
        "fresh": False,
        "profile": {
            "object_id" : str(player["_id"]),
            "created_at": player["created_at"],
            "updated_at": player["updated_at"],
            "user_id": player["user_id"],
            "nickname": player["nickname"]      
            },
        "uid": player["user_id"]
    }
    return jsonify(data), 200, {'Content-Type': 'application/json'}


@login.route("/user/profile", methods=['GET'])
def profile():
    FindPlayer=FindData(request.args.get("id"), request.remote_addr)
    data=FindPlayer.get_data_find_by_id()
    data={"code":0,"object_id":str(data["_id"]),"created_at":data["created_at"],"updated_at":data["updated_at"],"user_id": str(data["_id"]),"nickname":data["nickname"],"account":"","last_login_out_time":"0001-01-01T00:00:00Z","fresh":False}
    data=json.dumps(data, indent=2, sort_keys=True)
    return data, 200, {'Content-Type': 'application/json'}

@login.route("/statistics/login_statistics", methods=['GET', 'POST'])
def login_static():
    data = {"code": 0,"msg": "ok"}
    return data, 200, {'Content-Type': 'application/json'}

@login.route("/musedash/v1/ability")
def ability():
    data = {
        "code":0,
        "msg":"ok",
        "data":
        {
            "ability":0,
            "num":1
        }
    }
    return data, 200 , {'Content-Type': 'application/json'}
