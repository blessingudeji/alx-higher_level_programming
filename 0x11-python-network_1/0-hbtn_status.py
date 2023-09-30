#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    page = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(page) as response:
        show = response.read()

    print("Body response:")
    print("\t- type:", type(show))
    print("\t- content:", show)
    print("\t- utf8 content:", show.decode('utf-8'))
