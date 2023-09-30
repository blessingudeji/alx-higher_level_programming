#!/usr/bin/python3
""" Takes in a URL and an email address, sends
a POST request to the passed URL with the email
as a parameter, and finally displays the body
of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email_address = {"email": sys.argv[2]}

    page = requests.post(url, data=email_address)
    print(page.text)
