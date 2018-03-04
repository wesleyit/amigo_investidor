# -*- coding: utf-8 -*-


"""API is the module responsible for mantaining an Flask API
to respond requests to the chatbot."""


import json
from flask import Flask
from flask import request
from flask import make_response
import pandas as pd
app = Flask(__name__)


@app.route('/face_webhook', methods=['POST'])
def webhook():
    ping = request.get_json(silent=True, force=True)
    print('Request:')
    print(json.dumps(ping, indent=4))
    if ping['result']['metadata']['intentName'] == 'perfil_conservador':
        msg = conservative_profile()
    else:
        msg = bold_profile()
    pong = prepare(msg)
    pong = json.dumps(pong, indent=4)
    pong = make_response(pong)
    pong.headers['Content-Type'] = 'application/json'
    return pong


def read_saved_data():
    try:
        df = pd.read_csv('./temp.csv')
        return(df)
    except FileNotFoundError:
        return None


def conservative_profile():
    df = read_saved_data()
    selic = df['selic'][0]
    daily_factor = df['daily_factor'][0]
    cdi = df['cdi'][0]
    return """Para investimentos de baixo risco é sempre
bom acompanhar a Selic e o CDI.
Estar por dentro do fator diário também ajuda na hora de
diversificar na renda fixa.

*Selic: %s*
*CDI: %s*
*Fator Diário: %s*

E lembre-se: a poupança paga muito mal. Aventure-se :D
""" % (selic, cdi, daily_factor)


def bold_profile():
    df = read_saved_data()
    bitcoin = df['bitcoin'][0]
    dollar = df['dollar'][0]
    ibovespa = df['ibovespa'][0]
    nasdaq = df['nasdaq'][0]
    euro = df['euro'][0]
    return """O investidor de alto risco precisa estar por
dentro de tudo para não perder boas chances.

*Dollar: %s*
*Euro: %s*
*Bitcoin: %s*
*Ibovespa: %s*
*Nasdaq: %s*

E quando ficar milionário lembre-se deste humilde bot, tá? ;-)
""" % (dollar, euro, bitcoin, ibovespa, nasdaq)


def prepare(text):
    return {'messages': [{'speech': text, 'platform': 'facebook', 'type': 0}]}


if __name__ == '__main__':
    app.run(debug=False, port=8080, host='0.0.0.0')
