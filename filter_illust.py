#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import shutil
import cv2
import config

def filter_illust():
    # move to the repository
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )
    
    files = os.listdir("tmp")

    for f in files:
        filename = "tmp/" +  f
        faceCascade = cv2.CascadeClassifier(config.CASCADE_FILE)
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        if len(faces) == 0:
            os.remove(filename)
        if len(faces) == 1:
            x, y, w, h = faces[0]
            rate = w*h/(img.shape[0]*img.shape[1])
            if rate <= 0.02:
                os.remove(filename)

    if not os.path.exists("img"):
        os.mkdir("img")
        
    files = os.listdir("tmp")
    for f in files:
        filename = "tmp/" + f
        shutil.move(filename, "img")

    os.removedirs("tmp")

if __name__ == '__main__':
    filter_illust()
