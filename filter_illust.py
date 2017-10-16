#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import cv2
import config

def filter_illust():
    files = os.listdir("img")

    for f in files:
        filename = "img/" + f
        faceCascade = cv2.CascadeClassifier(config.CASCADE_FILE)
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            os.remove(filename)

if __name__ == '__main__':
    filter_illust()
