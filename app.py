from flask import Flask, render_template, jsonify, make_response, request
import os
import api_calls

from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "pythonAPIProject"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###



@app.route("/")
def home():
    return jsonify("Please chose one of the valid paths: /Users, /Albums, /Users/:<string:userid>/albums, /swagger")

@app.route("/Users")
def api_users():
    return jsonify(api_calls.get_users())


@app.route("/Albums")
def api_albums():
    return jsonify(api_calls.get_albums())

@app.route("/Users/<int:userid>/albums")
def api_user_albums(userid):
    return jsonify(api_calls.get_user_albums(userid))



########Error Handlers#########
@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)
################################


# This is here as app.py is our main file
if __name__ == '__main__':
    app.run()