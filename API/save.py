from flask import Blueprint, jsonify, request, Response, url_for, redirect, session
import json

save=Blueprint('save', __name__)


def jsonResponseFactory(data):
    '''Return a callable in top of Response'''
    def callable(response=None, *args, **kwargs):
        '''Return a response with JSON data from factory context'''
        return Response(json.dumps(data), *args, **kwargs)
    return callable


@save.route("/musedash/v2/save", methods=['GET'])
def SaveGet():
    print(request.headers)
    print(request.get_data())
    print("-------------------data hello???????????????????????????")
    data = {"code": 0,"msg": "ok"}
    return data, 200, {'Content-Type': 'application/json'}
