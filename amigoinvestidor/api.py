# -*- coding: utf-8 -*-


"""API is the module responsible for mantaining an Flask API
to respond requests to the chatbot."""


import json
from flask import Flask
from flask import request
from flask import make_response
app = Flask(__name__)


@app.route('/face_webhook', methods=['POST'])
def webhook():
    ping = request.get_json(silent=True, force=True)
    print("Request:")
    print(json.dumps(ping, indent=4))
    pong = "O cavalo morto... ah, vc já sabe."
    pong = json.dumps(pong, indent=4)
    pong = make_response(pong)
    pong.headers['Content-Type'] = 'application/json'
    return pong


if __name__ == "__main__":
    app.run(debug=False, port=8080, host='0.0.0.0')
