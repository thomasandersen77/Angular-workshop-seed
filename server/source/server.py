#!/usr/bin/env python
# encoding: utf-8
from models import Tweet
from models import User
from flask import Flask
from flask.ext.restful import Resource
from flask.ext.restful import Api

from flask import jsonify
from flask import abort
from flask import request
from custom_decorators import crossdomain


app = Flask(__name__)
api = Api(app)

db = {'tweets': [], 'users': []}  # KISS


def validate_user(data):
    if 'user' not in data:
        return jsonify(status=400, message="no user object"), 400
    if 'username' not in data['user']:
        return jsonify(status=400, message="no username in 'user'"), 400
    if 'password' not in data['user']:
        return jsonify(status=400, message="no password in 'user'"), 400

    return None


class Tweets(Resource):
    @crossdomain(origin="*")
    def get(self):
        return jsonify({"tweets": [t.serialize() for t in db['tweets']]})

    @crossdomain(origin="*")
    def options(self):
        return super(Tweets, self).options()

    @crossdomain(origin="*")
    def post(self):
        data = request.json

        validation_error = validate_user(data)
        if validation_error is not None:
            return validation_error

        user = get_user(data['user']['username'])
        if user is None:
            return jsonify(status=400, message="user does not exist")

        if user.password != data['user']['password']:
            return jsonify(status=403, message="incorrect password")

        text = data['text']
        if(len(text) > 140):
            return jsonify(status=400, message="tweet too long"), 400
        if(len(text) == 0):
            return jsonify(status=400, message="empty tweet"), 400

        for word in [u"#arsenal", u"#denfølelsen"]:
            if word in text.lower():
                abort(418)  # I am a teapot

        tweet = Tweet(user, text)
        db['tweets'].append(tweet)
        return jsonify(tweet.serialize()), 200


class TweetsUser(Resource):
    @crossdomain(origin="*")
    def get(self, username):
        user = get_user(username)
        if user is None:
            abort(404)

        app.logger.debug("getting tweets for: %s", user)

        return jsonify({"tweets": [t.serialize() for t in user.tweets]})

api.add_resource(Tweets, '/api/v1/tweets')
api.add_resource(TweetsUser, '/api/v1/tweets/<string:username>')


class UsersList(Resource):
    @crossdomain(origin="*")
    def get(self):
        return jsonify({"users": [u.serialize() for u in db['users']]})

    @crossdomain(origin="*")
    def options(self):
        return super(UsersList, self).options()

    @crossdomain(origin="*")
    def post(self):  # Register
        data = request.json

        validation_error = validate_user(data)
        if validation_error is not None:
            return validation_error

        # taken? if so 409 conflict!
        username = data['user']['username']
        for u in db['users']:
            if u.username == username:
                return jsonify(status=400,
                               message="user does already exist"), 400

        username = data['user']['username']
        password = data['user']['password']
        full_name = None
        if 'full_name' in data['user']:
            full_name = data['user']['full_name']

        user = User(username, password, full_name)
        db['users'].append(user)
        return jsonify(status=200), 200


class Users(Resource):
    @crossdomain(origin="*")
    def get(self, username):
        user = get_user(username)
        if user is None:
            abort(404)
        return jsonify({"users": user.serialize()}), 200


api.add_resource(UsersList, '/api/v1/users')
api.add_resource(Users, '/api/v1/users/<string:username>')


class UserCredentials(Resource):
    @crossdomain(origin="*")
    def options(self):
        return super(UserCredentials, self).options()

    @crossdomain(origin="*")
    def post(self):
        """
        Pretty much a dummy endpoint, check if username and password is correct
        """
        data = request.json

        validation_error = validate_user(data)
        if validation_error is not None:
            return validation_error

        user = get_user(data['user']['username'])
        if user is None:
            return abort(400, {status: 400, message: "user does not exist"})

        if user.password != data['user']['password']:
            return abort(403, {status: 403, message: "incorrect password"})

        return jsonify(status=200), 200


api.add_resource(UserCredentials, '/api/v1/login')


def get_user(username):
    for u in db['users']:
        if u.username == username:
            return u
    return None


if __name__ == '__main__':
    james = User("james", "password", full_name="James Ward")
    douglas = User("douglas", "password", full_name="Doublas Scott")

    db['users'].append(james)
    db['users'].append(douglas)

    db['tweets'].append(Tweet(james, "first!"))
    db['tweets'].append(Tweet(douglas, "@james firsts are stupid.."))
    app.run(debug=True, host='0.0.0.0', port=80)
