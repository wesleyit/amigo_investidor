# -*- coding: utf-8 -*-


"""API is the module responsible for mantaining an Flask API
to respond requests to the chatbot."""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
