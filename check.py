#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import cv2
import config

def filter_illust():
    # move to the repository
    os.chdir( os.path.dirname(os.path.abspath(__file__)) )
    
    files = os.listdir("img")

    for f in files:
        filename = "img/" + f
        faceCascade = cv2.CascadeClassifier(config.CASCADE_FILE)
        img = cv2.imread(filename)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        print('---')
        for (x, y, w, h) in faces:
            print(w*h / (img.shape[0]*img.shape[1]))
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Faces found", img)
        cv2.waitKey(0)

if __name__ == '__main__':
    filter_illust()
