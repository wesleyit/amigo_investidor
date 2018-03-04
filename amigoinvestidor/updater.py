# -*- coding: utf-8 -*-


"""Updater is the package responsible for get new values from an
external API and refresh the local file with updated financial
indexes and currency pricing."""


from requests import get
from os import environ
from pandas import DataFrame
from time import time, sleep
import schedule


def get_data():
    """Connects to the API provider and gets the current values.
    Returns a JSON."""
    API_KEY = environ.get('API_KEY')
    url = "https://api.hgbrasil.com/finance?format=json&key=%s" % API_KEY
    result = get(url)
    return result.json()


def parse_fields(results):
    """Extracts the necessary fields from the requested JSON.
    Returns a dictionary with the selected values."""
    fields = {}
    r = results['results']
    print(r)
    fields['cdi'] = r['taxes'][0]['cdi']
    fields['selic'] = r['taxes'][0]['selic']
    fields['daily_factor'] = r['taxes'][0]['daily_factor']
    fields['ibovespa'] = r['stocks']['IBOVESPA']['variation']
    fields['nasdaq'] = r['stocks']['NASDAQ']['variation']
    fields['dollar'] = r['currencies']['USD']['buy']
    fields['euro'] = r['currencies']['EUR']['buy']
    fields['bitcoin'] = r['currencies']['BTC']['buy']
    fields['timestamp'] = time()
    return fields


def write_csv(fields, csv_file="./temp.csv"):
    """Writes the request content to a CSV local file.
    This will avoid making too many HTTP requests."""
    df = DataFrame.from_records([fields], index='timestamp')
    df.to_csv(csv_file)


def pipeline():
    """Runs everything in order."""
    results = get_data()
    fields = parse_fields(results)
    write_csv(fields)
    print('Pipeline finished.')


def main_loop():
    """This block will loop forever and execute the pipeline
    function every 60 minutes."""
    pipeline()
    schedule.every().hour.do(pipeline)
    while True:
        schedule.run_pending()
        sleep(1)


if __name__ == '__main__':
    main_loop()
