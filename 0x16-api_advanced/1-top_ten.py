#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of .
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If, print None.
    """
    thereq = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if thereq.status_code == 200:
        for get_data in thereq.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)
