from flask import Blueprint, jsonify, request
from flaskapp.api.resources import WelcomeAPI, IBRA_API, IUCN_API, SUNBURST_API

# Initiating API blueprint
api_bp = Blueprint('api', __name__)


# Intializing API routes function used when intializing the app
def initialise_api_routes(api):
    api.add_resource(IBRA_API, '/api/ibra')
    api.add_resource(IUCN_API, '/api/iucn')
    api.add_resource(SUNBURST_API, '/api/sunburst')
    api.add_resource(WelcomeAPI, '/api')