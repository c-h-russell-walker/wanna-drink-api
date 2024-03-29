import json

from flask import jsonify, request

from app import app
from exceptions import InvalidUsage
from services import create_account
from models import WannaUser

# TODO - figure out if there's a way to not have to prefix all routes with 'api'

@app.route('/api/account', methods=['GET'])
def account():
    # Bundled with sign in most likely
    pass


@app.route('/api/account', methods=['POST'])
def post_to_account():
    try:
        user_form = request.form.copy()
        assert WannaUser.is_valid(user_form)

        user = WannaUser(user_form)
        # TODO - check if we have one - create it or update
        create_account(user)
    except Exception as exc:
        raise InvalidUsage(exc.message, status_code=400)

    return jsonify({'status_code': 200, 'success': True})


@app.route('/api/styles', methods=['GET'])
def get_beer_styles():
    with open('fixtures/beer_styles.json') as data_file:
        beer_styles = json.load(data_file)
    # TODO - alter data for the use we want - fixture JSON is actual response from API

    return jsonify(beer_styles)
