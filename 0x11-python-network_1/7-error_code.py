#!/usr/bin/python3
""" Error code #1 """


import sys
import requests


if __name__ == "__main__":
    link = sys.argv[1]

    res = requests.get(link)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
