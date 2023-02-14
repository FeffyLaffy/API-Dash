from flask import Blueprint, jsonify, request, Response, url_for, redirect, session

statistics = Blueprint('statistics', __name__)


@statistics.route("/statistics/pc-play-statistics-feedback", methods=['POST'])
def pcPlayStatsFeedback():
    return

@statistics.route("/statistics/achievement-statistics-feedback", methods=['POST'])
def pcPlayGetAchievementFeedback():
    return
