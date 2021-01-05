from flaskapp import db
from flask_restful import Resource
from flask import request

'''
EXAMPLE
from flaskapp.main.models import Message

# Marshmallow MessageSchema
class MessageSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Message

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    phone = ma.auto_field()
    body = ma.auto_field()
    date_submitted = ma.auto_field()


# Initaiting MessageSchema, one for all messages, the other for particular messages
messages_schema = MessageSchema(many=True)
message_schema = MessageSchema()


class MessagesAPI(Resource):
    # Defining get to get messages according to their 'id' in acending order
    def get(self):
        messages = Message.query.order_by(Message.id.asc()) # dumping the message according to the message_schema
        ret = ({'messages': messages_schema.dump(messages)}, 200) # respond with the data and a 200 approved message
        return ret[0], ret[1]
''' 