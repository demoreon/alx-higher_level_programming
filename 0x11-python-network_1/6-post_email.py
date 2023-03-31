#!/usr/bin/python3
""" POST an email #1 """


import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}

    res = requests.post(link, data=val)
    print(res.text)
