from flask import Blueprint, jsonify, request, Response, url_for, redirect, session

statistics = Blueprint('statistics', __name__)


@statistics.route("/statistics/pc-play-statistics-feedback", methods=['POST'])
def pcPlayStatsFeedback():
    return

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


