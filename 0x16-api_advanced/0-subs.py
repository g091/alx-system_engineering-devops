#!/usr/bin/python3
""" Function that queries the Reddit API & returns the no. of subscribers
	for a given subreddit. If an invalid subreddit is given, the function
	should return 0."""

import requests as rq


def number_of_subscribers(subreddit):
    """ Returns the no. of subs"""
    if subreddit:
        res = rq.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'Python/requests:APIproject:\
v1.0.0 (by /u/aaorrico23)'}).json()
        sub = res.get("data", {}).get("subscribers", 0)
        return sub
    return 0
