#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `amigoinvestidor` package."""


import pytest
from json import load
import amigoinvestidor.updater as upd
headers = \
    'timestamp,bitcoin,cdi,daily_factor,dollar,euro,ibovespa,nasdaq,selic\n'
tmp_file = '/tmp/amigoinvestidor_test.csv'


@pytest.fixture()
def prepare_data():
    with open('tests/sample_reply.json') as json_file:
        sample_json = load(json_file)
    data = upd.get_data()
    fields = upd.parse_fields(sample_json)
    upd.write_csv(fields, csv_file=tmp_file)
    return (sample_json, data, fields)


def test_get_data():
    _, data, _ = prepare_data()
    assert type(data) == dict


def test_parse_fields():
    _, _, fields = prepare_data()
    assert fields['dollar'] == 3.2506


def test_write_csv():
    _, _, fields = prepare_data()
    upd.write_csv(fields, csv_file=tmp_file)
    with open(tmp_file) as f:
        line = f.readline()
    assert line == headers
