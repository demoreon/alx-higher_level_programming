#!/usr/bin/python3
"""A  script that:
- takes in a URL and an email address
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}

    res = requests.post(link, data=val)
    print(res.text)
