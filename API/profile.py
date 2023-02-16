from flask import Blueprint, jsonify, request, Response, url_for, redirect, session

profile = Blueprint('profile', __name__)


@profile.route("/user/profile", methods=['POST'])
def EditProfile():
    return

