''' #!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `amigoinvestidor` package."""

from json import load
import amigoinvestidor.amigoinvestidor as amigo


headers = 'timestamp,bitcoin,cdi,daily_factor,dolar,euro,ibovespa,nasdaq,selic'
with open('tests/sample_reply.json') as json_file:
    sample_json = load(json_file)


def test_get_data():
    data = amigo.get_data()
    print(data)
    data_type = type(data)
    assert data_type == dict


def test_parse_fields():
    fields = amigo.parse_fields(sample_json)
    assert fields['dollar'] == 3.2506


def test_write_csv():
    fields = amigo.parse_fields(sample_json)
    amigo.write_csv(fields, csv_file='/tmp/teste.csv')
    with open('/tmp/teste.csv') as tmp_file:
        line = tmp_file.readline()
    assert line == headers
 '''
