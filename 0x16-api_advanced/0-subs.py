#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    """  Args:
        subreddit: subreddit name
    Returns:
        number of subscribers to the subreddit,
        or 0 if subreddit requested is invalid
        """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': '0x16-api_advanced (by u/na-cho-dev)'}

    sub_info = requests.get(url,
                            headers=headers,
                            allow_redirects=False)

    if sub_info.status_code >= 300:
        return 0

    return sub_info.json().get("data").get("subscribers")
