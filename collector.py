#!/usr/bin/python3
# -*- coding:utf-8 -*-

import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET

twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/search/tweets.json"

keyward = "ゆゆ式"

params = {'1': keyward, 'count': 5}

req = twitter.get(url, params = params)

if req.status_code == 200:
    search_timeline = json.loads(req.text)
    for tweet in search_timeline['statuses']:
        print(tweet['text'])
else:
    print("ERROR: %d" % req.status_code)
