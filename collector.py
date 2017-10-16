#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import config
import json
import requests
import os
import pickle
from history import history
from requests_oauthlib import OAuth1Session

def save_image(url, tweet_url):
    # move to the repository
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )
        
    # load history
    hist = history()
    if os.path.exists("misc/history.pickle"):
        with open("misc/history.pickle", "rb") as f:
            hist = pickle.load(f)

    # save images
    basename = os.path.basename(url)
    filepath = "img/" + basename
    if not hist.contains(basename):
        hist.append(tweet_url, basename)
        r = requests.get(url)
        if r.status_code == 200:
            content_type = r.headers["content-type"]
            if "image" in content_type:
                # save an image
                if not os.path.isdir("img"):
                    os.mkdir("img")
                with open(filepath, "wb") as f:
                    f.write(r.content)

    # save history
    with open("misc/history.pickle", "wb") as f:
        pickle.dump(hist, f)

def collect_list(search_list):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = "https://api.twitter.com/1.1/search/tweets.json"

    keyward = "filter:images list:" + search_list

    params = {'q': keyward, 'count': config.SEARCH_COUNT}

    req = twitter.get(url, params = params)

    if req.status_code == 200:
        search_timeline = json.loads(req.text)
        for tweet in search_timeline['statuses']:
            if 'media' in tweet['entities']:
                for media in tweet['entities']['media']:
                    save_image(media['media_url'], media['expanded_url'])
    else:
        print("ERROR: %d" % req.status_code)

def collect_lists():
    for li in config.SEARCH_LIST:
        collect_list(li)
        
if __name__ == "__main__":
    collect_lists()
