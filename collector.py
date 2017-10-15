#!/usr/bin/python3
# -*- coding:utf-8 -*-

import config
import json
import argparse
import requests
import os
import pickle
from requests_oauthlib import OAuth1Session

def save_image(url):
    max_history = 100
    history = []
    if os.path.exists("misc/history"):
        with open("misc/history", "rb") as f:
            history = pickle.load(f)
    filename = "img/" + os.path.basename(url)
    if url not in history:
        history.append(url)
        if len(history) > max_history:
            history.pop(0)
        r = requests.get(url)
        if r.status_code == 200:
            content_type = r.headers["content-type"]
            if "image" in content_type:
                with open(filename, "wb") as f:
                    f.write(r.content)
    with open("misc/history", "wb") as f:
        pickle.dump(history, f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', '-l', type=str, default="joisino_/pri")
    parser.add_argument('--count', '-c', type=int, default=20)
    args = parser.parse_args()

    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = "https://api.twitter.com/1.1/search/tweets.json"

    keyward = "filter:images list:" + args.list

    params = {'q': keyward, 'count': args.count}

    req = twitter.get(url, params = params)

    if req.status_code == 200:
        search_timeline = json.loads(req.text)
        for tweet in search_timeline['statuses']:
            if 'media' in tweet['entities']:
                for media in tweet['entities']['media']:
                    save_image(media['media_url'])
    else:
        print("ERROR: %d" % req.status_code)

if __name__ == "__main__":
    main()
