from flask import Blueprint, jsonify, request, Response, url_for, redirect, session

statistics = Blueprint('statistics', __name__)


@statistics.route("/statistics/pc-play-statistics-feedback", methods=['POST'])
def pcPlayStatsFeedback():
    """
    {
        "character_name": "凛-贝斯手",
        "character_uid": "0",
        "controller_name": "KeyboardA0",
        "elfin_name": null,
        "elfin_uid": null,
        "music_level": 1,
        "music_name": "Magical Wonderland (More colorful mix)",
        "music_uid": "0-48",
        "player": "4efdeb974ba5431487fd6ea19dd5c9bf",
        "player_level": 1,
        "result_acc": 78.0,
        "result_combo": 46,
        "result_finished": true,
        "result_full_combo": false,
        "result_score": 37690
    }
    """
    data = request.get_json(force=True)
    return {
        "code": 0,
        "id": "63eb63a6239db258b7cf4bd9",
        "msg": "ok"
    }


@statistics.route("/statistics/achievement-statistics-feedback", methods=['POST'])
def pcPlayGetAchievementFeedback():
    return


@statistics.route("/statistics/favorite_music", methods=['POST'])
def PlayerSetFavoriteMusic():
    return


@statistics.route("/statistics/login_statistics", methods=['POST'])
def pcStats():
    return


@statistics.route("/statistics/challenge-statistics-feedback", methods=['POST'])
def pcPlayGetChallengeFeedback():
    return
