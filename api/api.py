from flask import Flask
from flask_restful import abort, fields, marshal_with, reqparse, Resource, Api
from datetime import datetime as dt
from pytz import utc
from models import MessageModel
import status


class MessageManager():
    last_id = 0;
    def __init__(self):
        self.messages = {}

    def insert_message(self, message):
        self.__class__.last_id += 1
        message.id = self.__class__.last_id
        self.messages[self.__class__.last_id] = message

    def get_message(self, id):
        return self.messages[id]

    def delete_message(self, id):
        del self.messages[id]

    