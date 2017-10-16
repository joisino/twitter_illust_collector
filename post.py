#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import config
import slackweb
import os
import pickle
from history import history

def post():
    # move to the repository
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )
    
    slack = slackweb.Slack(url=config.SLACK_URL)

    hist = history()
    with open("misc/history.pickle", "rb") as f:
        hist = pickle.load(f)
    
    files = os.listdir("img")
    for f in files:
        slack.notify(text=hist.get_url(f))
        os.remove("img/" + f)

    os.removedirs("img")
    
if __name__ == "__main__":
    post()
