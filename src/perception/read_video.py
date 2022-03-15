#!/usr/bin/env/python
import numpy as np
import cv2

#video_capture = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture("videos/Planner.mp4")

while(True):
    ret, frame = video_capture.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame, (0, 0), fx=1.5, fy=1.5)
    cv2.line(frame, (0, 0), (100, 100), (255, 0, 0), 5)
    cv2.imshow("Frame", frame)
    if(cv2.waitKey(1000) & 0xFF == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()
