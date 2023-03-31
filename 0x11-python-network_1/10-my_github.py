#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password) """


import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    sec = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=sec)
    print(res.json().get("id"))
