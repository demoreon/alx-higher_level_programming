#!/usr/bin/python3
""" Response header value #1 """


import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    res = requests.get(link)
    print(res.headers.get("X-Request-Id"))
