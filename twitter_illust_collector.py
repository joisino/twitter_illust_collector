#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collector import collect_list
from filter_illust import filter_illust
from post import post

if __name__ == "__main__":
    collect_list()
    filter_illust()
    post()