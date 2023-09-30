#!/usr/bin/python3
"""Takes in a URL and an email"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email_address = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email_address).encode("ascii")

    page = urllib.request.Request(url, data)
    with urllib.request.urlopen(page) as response:
        print(response.read().decode("utf-8"))
