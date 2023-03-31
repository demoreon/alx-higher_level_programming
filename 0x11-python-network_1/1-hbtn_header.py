#!/usr/bin/python3
"""A script that:
This Python script takes in a URL then displays the value of the X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    link = sys.argv[1]

    response = urllib.request.Request(link)
    with urllib.request.urlopen(link) as res:
        print(dict(res.headers).get("X-Request-Id"))
