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


#data we want to render to messageModel class (JSON representation)
message_fields = {
    'id': fields.Integer,
    'uri': fields.Url('message_endpoint'),
    'message': fields.String,
    'duration': fields.Integer,
    'creation_date': fields.DateTime,
    'message_category': fields.String,
    'printed_times': fields.Integer,
    'printed_once': fields.Boolean
}

message_manager = MessageManager()
