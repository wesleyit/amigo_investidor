# -*- coding: utf-8 -*-


"""Amigo Investidor (amigoinvestidor) package."""


__author__ = """Wesley Rodrigues da Silva"""
__email__ = 'wesley.it@gmail.com'
__version__ = '0.1.0'


from .updater import (get_data, write_csv, parse_fields)


__all__ = ['get_data', 'write_csv', 'parse_fields']
