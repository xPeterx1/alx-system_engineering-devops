#!/usr/bin/python3
"""Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """number of subscribers"""

    theheaders = {'User-Agent': 'MyPythonScript/1.0'}
    therequest = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json", headers=theheaders)

    if therequest.status_code == 200:
        subscribers = therequest.json().get('data').get('subscribers')
        return subscribers if subscribers else 0
    return 0
