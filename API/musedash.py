from flask import Blueprint

musedash = Blueprint('musedash', __name__)

ldata = {
    "code": 0,
    "rank": {
        "detail": None,
        "order": None
    },
    "result": [
        {
            "play": {
                "acc": 101,
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
                "score": 9000000,
                "updated_at": "2021-08-22T07:23:06.079Z",
                "user_id": "bdc11ba2a21711e9ad070242ac110025",
                "visible": True
            },
            "user": {
                "created_at": "2019-07-09T07:04:06.307Z",
                "nickname": "Looz",
                "object_id": "5d243c66a673f50069ef55d5",
                "updated_at": "2021-02-05T10:29:04.133Z",
                "user_id": "bdc11ba2a21711e9ad070242ac110025"
            }
        }
    ]
}


@musedash.route("/musedash/v1/pcleaderboard/top", methods=['GET'])
def ori_board():
    return ldata, 200, {'Content-Type': 'application/json'}
