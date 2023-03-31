#!/usr/bin/python3
""" Evaluation/interview coding """


import sys
import requests

if __name__ == "__main__":
    link = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    res = requests.get(link)
    coms = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                coms[i].get("sha"),
                coms[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
