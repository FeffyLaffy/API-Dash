from flask import Blueprint
import json

config=Blueprint('config', __name__)

adata=open('announce.json', 'rb')
adata= json.load(adata)
data=open('music_tag.json', 'rb')
music_tag_data= json.load(data)
data=open('anchor.json', 'rb')
anchor= json.load(data)

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

@config.route("/musedash/v1/music_tag", methods=['GET'])
def music_tag():
    return music_tag_data, 200 , {'Content-Type': 'application/json'}

@config.route("/musedash/v1/anchor", methods=['GET'])
def anchor():
    return anchor, 200, {'Content-Type': 'application/json'}

@config.route("/musedash/v1/module_config", methods=['GET'])
def module_config():
    return config_mod, 200, {'Content-Type': 'application/json'}

@config.route("/musedash/announce/pc", methods=['GET'])
def annouce():
    return adata, 200 , {'Content-Type': 'application/json'}