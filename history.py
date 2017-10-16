#!/usr/bin/python3
# -*- coding:utf-8 -*-

class history():
    def __init__(self):
        self.max_history = 100
        self.history = []
        self.dict = {}

    def append(self, url, basename):
        self.history.append(basename)
        if len(self.history) > self.max_history:
            self.dict.pop(self.history[0])
            self.history.pop(0)
        self.dict[basename] = url

    def contains(self, basename):
        return basename in self.history

    def get_url(self, basename):
        return self.dict[basename]
