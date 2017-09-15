import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
width = 1080
cv2.namedWindow("frame", 0)
cv2.resizeWindow("frame", width, 768)

image_path_name = 'images/shot.png'


def recognize(image_path_name):
    visual_recognition = VisualRecognitionV3('2016-05-20', api_key='38101248a17c138c02f3e9c20052f04af5b3a61a')
    # {38101248a17c138c02f3e9c20052f04af5b3a61a}
    # print(json.dumps(visual_recognition.classify(images_file='SteinTest.jpg'), indent = 2))


    path = join(dirname(__file__), image_path_name)
    with open(path, 'rb') as images_file:
        results = visual_recognition.classify(images_file=images_file,
                                              classifier_ids=[
                                                  'schnickschnackschnuck_699533305'])

    return results


while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        ts = time.time()
        r = 1080.0 / frame.shape[1]
        dim = (1080, int(frame.shape[0] * r))

        # perform the actual resizing of the image and show it
        resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite(image_path_name, resized)

        results = recognize(image_path_name)

        print(json.dumps(results, indent=2))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# image_name = 'SteinTest.jpg'
# results = recognize(image_name)
# print(json.dumps(results, indent=2))
