#!/usr/bin/python3
"""Module for task 3"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    """
    import requests

    sob_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sob_info.status_code != 200:
        return None

    Info = sob_info.json()

    los_l = [child.get("data").get("title")
             for child in Info
             .get("data")
             .get("children")]
    if not los_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in los_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not Info.get("data").get("after"):
        Nsorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        Nsorted_counts = sorted(word_count.items(),
                                key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in Nsorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           Info.get("data").get("after"))
