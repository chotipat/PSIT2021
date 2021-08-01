"""Docstring file"""
import sys

import requests

r = requests.get('https://www.google.com')

print(r.status_code)
print(sys.version)
print(sys.executable)


def test():
    """ Docstring """
    print("test")

test()
