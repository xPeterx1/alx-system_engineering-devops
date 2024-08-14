#!/usr/bin/python3
"""
Script that on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total  on a given subreddit."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    theheaders = {"User-Agent": "Linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    theresponse = requests.get(url, headers=theheaders, allow_redirects=False)
    if theresponse.status_code == 404:
        return 0
    results = theresponse.json().get("data")
    return results.get("subscribers")
