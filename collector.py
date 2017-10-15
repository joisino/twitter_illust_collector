#!/usr/bin/python3
# -*- coding:utf-8 -*-

import config
import json
import argparse
import requests
import os
from requests_oauthlib import OAuth1Session

def save_image(url):
    r = requests.get(url)
    if r.status_code == 200:
        content_type = r.headers["content-type"]
        if "image" in content_type:
            filename = "img/" + os.path.basename(url)
            with open(filename, "wb") as f:
                f.write(r.content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', '-l', type=str, default="joisino_/pri")
    args = parser.parse_args()

    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET

    twitter = OAuth1Session(CK, CS, AT, ATS)

    url = "https://api.twitter.com/1.1/search/tweets.json"

    keyward = "filter:images list:" + args.list

    params = {'q': keyward, 'count': 10}

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
