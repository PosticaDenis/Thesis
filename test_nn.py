# -*- coding: utf-8 -*-
"""
Created on Thu May 24 02:55:32 2018

@author: denis
"""
import cv2
import time
from tools.keyboard_controller import PressKey, ReleaseKey, W, A, D, Q, E
from models import inception_v3 as googlenet
from tools.keys import check_key
from tools.screen import get_screen

WIDTH = 90
HEIGHT = 80
LR = 1e-3
EPOCHS = 10
MODEL_NAME = ''
model = googlenet(WIDTH, HEIGHT, 1, LR, output = 6, model_name=MODEL_NAME)
#model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)

def p_key(key):
    PressKey(key)
    ReleaseKey(key)

def test_nn():
    for i in list(range(3))[::-1]:
        print(i+1)
        time.sleep(1)
    paused = False
    while(True):
        if not paused:
            screen = get_screen(region = (20, 150, 975, 850))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (WIDTH, HEIGHT))
            prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]
            print(prediction)
            turn_thresh = .75
            forward_thresh = .70
            if prediction[0] > forward_thresh:
                p_key(W)
            elif prediction[1] > turn_thresh:
                p_key(A)
            elif prediction[2] > turn_thresh:
                p_key(D)
            elif prediction[3] > turn_thresh:
                p_key(Q)
            elif prediction[4] > turn_thresh:
                p_key(E)
            else:
                p_key(W)
        keys = check_key()
        if 'P' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

test_nn()       
