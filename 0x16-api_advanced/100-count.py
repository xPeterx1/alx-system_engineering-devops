#!/usr/bin/python3
"""Module for task 3"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    enfo = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in enfo
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for titl in hot_l:
        ssplit_words = titl.split(' ')
        for word in word_list:
            for ll_word in ssplit_words:
                if ll_word.lower() == word.lower():
                    word_count[word] += 1

    if not enfo.get("data").get("after"):
        sort_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sort_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sort_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           enfo.get("data").get("after"))
