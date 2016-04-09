from flask import Flask, jsonify

from exceptions import InvalidUsage

app = Flask(__name__)
# TODO - update in order to use dynamic Env. settings (prod, etc) when the time comes
app.config.from_object('config.common')

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

