import json
from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3

import numpy as np
import cv2
import time

import sys
import time

from random import randint

'''
'''
domain = ["rock", "paper", "scissors"]
result_p1_wins = "Player 1 wins!"
result_p2_wins = "Player 2 wins!"


def game_logic(player_1, player_2):
    if player_1 in domain and player_2 in domain:

        if player_1 == player_2:
            return ("No winner!")
        else:
            if player_1 == "paper":
                if player_2 == "rock":
                    return (result_p1_wins)
                else:
                    return (result_p2_wins)

            if player_1 == "rock":
                if player_2 == "scissors":
                    return (result_p1_wins)
                else:
                    return (result_p2_wins)

            if player_1 == "scissors":
                if player_2 == "paper":
                    return (result_p1_wins)
                else:
                    return (result_p2_wins)
    else:
        return ("Random error")


def label_2_int(lbl):
    return {
        'rock': 0,
        'paper': 1,
        'scissors': 2
    }[lbl]


def int_2_label(nmbr):
    return {
        0: 'rock',
        1: 'paper',
        2: 'scissors'
    }[nmbr]


def random_play():
    number = randint(0, len(domain) - 1)
    label = int_2_label(number)
    return label;


def play_series(player_1, player_2):
    player_1_wins = 0
    player_2_wins = 0
    for i in range(len(player_1)):
        result = game_logic(player_1[i], player_2[i])
        print(str(i) + ' | player 1: ' + player_1[i] + '\t player 2: ' + player_2[i] + '\t | ' + result)
        if (result == result_p1_wins):
            player_1_wins = player_1_wins + 1
        if (result == result_p2_wins):
            player_2_wins = player_2_wins + 1
    print('\nplayer 1: ' + str(player_1_wins) + ' win(s)\t player 2: ' + str(player_2_wins) + ' win(s)')


def play_game(player_1):
    player_2 = [random_play() for i in range(len(player_1))]
    play_series(player_1, player_2)

'''
'''

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


def log(j):
    j['images']



# play_game(['scissors', 'rock', 'rock', 'rock', 'paper'])

tr = {}
tr['Stein'] = 'rock'
tr['Schere'] = 'scissors'
tr['Papier'] = 'paper'

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

        if results['images'][0].get('classifiers'):
            res = results['images'][0]['classifiers'][0]['classes'][0]['class']
        else:
            print('Nix gefunden, kein Spiel möglich')
            player_2 = tr[res]

            play_game([player_2])
        # print(res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

# image_name = 'SteinTest.jpg'
# results = recognize(image_name)
# print(json.dumps(results, indent=2))

