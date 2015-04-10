# encoding: utf-8
from datetime import datetime


class Tweet(object):
    user = None
    text = ""
    timestamp = None

    def __init__(self, user, text):
        self.user = user
        self.text = text
        self.timestamp = datetime.now()

        self.user.tweets.append(self)

    def serialize(self):
        return {'username': self.user.username,
                'text': self.text,
                'timestamp': self.timestamp.isoformat()}

    def __repr__(self):
        return "<Tweet: %s, %s>" % (self.user, self.timestamp.isoformat())


class User(object):
    username = ""
    password = ""
    full_name = ""
    tweets = None

    def __init__(self, username, password, full_name=""):
        self.username = username
        self.password = password
        self.full_name = full_name
        self.tweets = []

    def serialize(self):
        return {'username': self.username,
                'full_name': self.full_name}

    def __repr__(self):
        return "<User: %s>" % self.username
