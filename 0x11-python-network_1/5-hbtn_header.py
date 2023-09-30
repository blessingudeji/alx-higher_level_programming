#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    page = requests.get(url)
    print(page.headers.get("X-Request-Id"))
