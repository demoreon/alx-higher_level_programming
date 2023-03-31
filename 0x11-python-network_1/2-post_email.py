#!/usr/bin/python3
"""A script that posts an email """


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    link = sys.argv[1]
    val = {"email": sys.argv[2]}
    res = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(link, res)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
