#!/usr/bin/python3
"""A script tha:
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    pchar = "" if len(sys.argv) == 1 else sys.argv[1]
    pload = {"q": pchar}

    res = requests.post("http://0.0.0.0:5000/search_user", data=pload)
    try:
        rres = res.json()
        if rres == {}:
            print("No result")
        else:
            print("[{}] {}".format(rres.get("id"), rres.get("name")))
    except ValueError:
        print("Not a valid JSON")
