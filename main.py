from datetime import datetime, timedelta
from lib2to3.pgen2 import token
from sqlite3 import Timestamp
from tkinter.messagebox import NO
import ssl
from flask import Flask, jsonify, request, Response, url_for, redirect, session
import json
import os
from functools import wraps
import requests
from pip._vendor import cachecontrol
import requests
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
adata=None
music_tag_data=None
anchor=None
oauth = OAuth(app)
app.secret_key = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!/xd5\xa2\xa0\x9fR"\xa1\xa8'
dataplayer={}

def jsonResponseFactory(data):
    '''Return a callable in top of Response'''
    def callable(response=None, *args, **kwargs):
        '''Return a response with JSON data from factory context'''
        return Response(json.dumps(data), *args, **kwargs)
    return callable

def is_ban(a):
    ban={"ban":a,"code":0,"msg":"ok"}
    return ban
    
ldata={
    "code": 0,
    "rank": {
        "detail": None,
        "order": None
    },
    "result": [
        {
            "play": {
                "acc": 100,
                "bms_id": 2163202,
                "bms_version": "",
                "character_uid": "3",
                "combo": 398,
                "created_at": "2021-02-06T11:52:51.231Z",
                "elfin_uid": "6",
                "hp": 200,
                "is_check": False,
                "judge": "sss",
                "miss": 0,
                "music_difficulty": 0,
                "music_uid": "33-2",
                "object_id": "601e831340fadf252be699ab",
                "score": 727727,
                "updated_at": "2021-08-22T07:23:06.079Z",
                "user_id": "bdc11ba2a21711e9ad070242ac110025",
                "visible": True
            },
            "user": {
                "created_at": "2019-07-09T07:04:06.307Z",
                "nickname": "Konishi",
                "object_id": "5d243c66a673f50069ef55d5",
                "updated_at": "2021-02-05T10:29:04.133Z",
                "user_id": "bdc11ba2a21711e9ad070242ac110025"
            }
        }
    ]
}

config_mod = {
  "code": 0,
  "module_config_list": [
    {
      "object_id": "61515c9b8da1e89777bb2399",
      "created_at": "2021-09-27T05:54:35.619Z",
      "updated_at": "2021-09-27T05:54:37.636Z",
      "config_name": "DerivativesMall",
      "config_state": True,
      "note": "周边商场控制开关"
    },
    {
      "object_id": "61515caf8da1e89777bb23f9",
      "created_at": "2021-09-27T05:54:55.955Z",
      "updated_at": "2022-01-27T06:09:40.937Z",
      "config_name": "anchor",
      "config_state": True,
      "note": "主播模式开关"
    },
    {
      "object_id": "61515fbe9760e2a561442726",
      "created_at": "2021-09-27T06:07:58.455Z",
      "updated_at": "2021-09-27T06:07:58.455Z",
      "config_name": "binding",
      "config_state": True,
      "note": "手机绑定模块"
    },
    {
      "object_id": "61515fdf8f547b4af9d9ead1",
      "created_at": "2021-09-27T06:08:31.795Z",
      "updated_at": "2021-09-27T06:08:33.319Z",
      "config_name": "mandatory-binding",
      "config_state": False,
      "note": "强制绑定"
    },
    {
      "object_id": "61b990132daddbfe4e08b426",
      "created_at": "2021-12-15T06:49:55.456Z",
      "updated_at": "2021-12-23T08:05:34.738Z",
      "config_name": "xd-pay",
      "config_state": False,
      "note": "线上xd开关，默认为关闭"
    }
  ]
}

def a(a):
    print(a)
    return

def time3(timestamp):
    time = {
    "code": 0,
    "data": {
        "server_time": timestamp
    }
    }
    return time

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = dict(session).get('profile', None)
        # You would add a check here and usethe user id or something to fetch
        # the other data for that user/check if they exist
        if user:
            return f(*args, **kwargs)
        return 'You aint logged in, no page for u!'
    return decorated_function


@app.route("/musedash/v1/pcleaderboard/top", methods=['GET'])
def leaderboard():
    print(request.query_string)
    return ldata, 200, {'Content-Type': 'application/json'}

@app.route("/musedash/announce/pc", methods=['GET'])
def annouce():
    return adata, 200 , {'Content-Type': 'application/json'}

@app.route("/musedash/v1/time", methods=['GET'])
def time():
    times=time3(int(round(datetime.utcnow().timestamp())))
    return times, 200 , {'Content-Type': 'application/json'}

@app.route("/musedash/v1/music_tag", methods=['GET'])
def music_tag():
    return music_tag_data, 200 , {'Content-Type': 'application/json'}

@app.route("/musedash/v1/anchor", methods=['GET'])
def anchor():
    return anchor, 200, {'Content-Type': 'application/json'}

@app.route("/musedash/v1/module_config", methods=['GET'])
def module_config():
    return config_mod, 200, {'Content-Type': 'application/json'}
 
@app.route('/oauth/google/login1', methods=['GET'])
def login_google():
 # Google Oauth Config
    # Get client_id and client_secret from environment variables
    # For developement purpose you can directly put it
    # here inside double quotes
    GOOGLE_CLIENT_ID = ""
    GOOGLE_CLIENT_SECRET = ""
    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )
    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

def jsonResponseFactory(data):
    '''Return a callable in top of Response'''
    def callable(response=None, *args, **kwargs):
        '''Return a response with JSON data from factory context'''
        return Response(json.dumps(data), *args, **kwargs)
    return callable

@app.route("/oauth/google/login", methods=['GET', 'POST'])
def google_auth():
    token = oauth.google.authorize_access_token()
    data={"code" : token["id_token"]}
    return redirect('http://us-musedash.peropero.net/api/v1/o/google/googleGetToken',200,jsonResponseFactory(data))

@app.route("/api/v1/o/google/googleGetToken", methods=['GET'])
def get_token():
    data={"code":0,"msg":"ok","data":{"token":request.args.get("code")}}
    return data, 200, {'Content-Type': 'application/json'}

def check_auth(token):
    player=open('player.json', 'rb')
    player= json.load(player)
    for key, values in player["data"].items():
        print("test"+token)
        print("test2"+key)
        if key==token:
            a={"auth": "a","code":0,"fresh":False,"profile":{"object_id":"62cfdae8c1dd5b7cfa114ef0","created_at":"2022-07-14T08:59:20.337Z","updated_at":"2022-07-14T08:59:20.337Z","user_id":"5abb7dfd33354edfa3703bc6073b3dac","nickname":"玩家5abb7dfd33354edfa3703bc6073b3dac"},"uid":"5abb7dfd33354edfa3703bc6073b3dac"}
            return a

@app.route('/user/account-oversea-login/', methods=['GET', 'POST'])
def acc_oversea_login():
    if request.method == "POST":

        return 404
    elif request.method == "GET":
        print(request.headers)
        return 202

@app.route("/user/profile")
def profile():
    if request.method == "POST":
        print(request.query_string)
        data={"code":0,"msg":"ok","profile":{"object_id":"62cfdae8c1dd5b7cfa114ef0","created_at":"2022-07-14T08:59:20.337Z","updated_at":"2022-07-14T08:59:20.337Z","user_id":"5abb7dfd33354edfa3703bc6073b3dac","nickname":"asatako"}}
        return data, 202, {'Content-Type': 'application/json'}
    elif request.method == "GET":
        data={"code":0,"msg":"ok","profile":{"object_id":"62cfdae8c1dd5b7cfa114ef0","created_at":"2022-07-14T08:59:20.337Z","updated_at":"2022-07-14T08:59:20.337Z","user_id":"5abb7dfd33354edfa3703bc6073b3dac","nickname":"asatako"}}
        return data, 202, {'Content-Type': 'application/json'}

#@app.route("musedash/v2/save", methods=['PUT'])
#def save():
  #  return 202

@app.route("/statistics/pc-play-statistics-feedback", methods=["POST"])
def pc_play():
    print(request.args.values)
    data={"msg": 202}
    return data, 202, {'Content-Type': 'application/json'}


@app.route("/statistics/challenge-statistics-feedback", methods=["POST"])
def challenge():
    print(request.args.values)
    data={"msg": 202}
    return data, 202, {'Content-Type': 'application/json'}

@app.route("/statistics/achievement-statistics-feedback", methods=["POST"])
def achievement():
    print(request.args.values)
    data={"msg": 202}
    return data, 202, {'Content-Type': 'application/json'}

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.load_cert_chain('konishi.crt', 'konishi.key')

if __name__ == "__main__":
    adata=open('announce.json', 'rb')
    adata= json.load(adata)
    data=open('music_tag.json', 'rb')
    music_tag_data= json.load(data)
    data=open('anchor.json', 'rb')
    anchor= json.load(data)
    app.run(host='0.0.0.0', port=443, ssl_context=context, debug=True)