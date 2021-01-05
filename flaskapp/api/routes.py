from flask import Blueprint, jsonify, request
# from flaskapp.api.resources import MessagesAPI, MessageAPI, UsersAPI
from flaskapp import app

# Initiating API blueprint
api_bp = Blueprint('api', __name__)

'''
Example
# Intializing API routes function used when intializing the app
def initialise_api_routes(api):
    api.add_resource(MessagesAPI, '/api/messages')
'''
    