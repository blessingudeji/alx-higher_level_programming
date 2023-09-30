#!/usr/bin/python3
""" Displays the value of the X-Request-Id"""
from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    page = request.Request(url)
    with request.urlopen(page) as response:
        print(dict(response.headers).get("X-Request-Id"))
