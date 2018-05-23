# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:13:32 2018

@author: denis
"""

import os
import numpy as np
import cv2
import time
from tools.keys import check_key
from tools.screen import get_screen

forward = [1,0,0,0,0,0,0,0,0]
reverse = [0,1,0,0,0,0,0,0,0]
full_left = [0,0,1,0,0,0,0,0,0]
full_right = [0,0,0,1,0,0,0,0,0]

left = [0,0,0,0,1,0,0,0,0]
right = [0,0,0,0,0,1,0,0,0]
r_left = [0,0,0,0,0,0,1,0,0]
r_right = [0,0,0,0,0,0,0,1,0]
no_key = [0,0,0,0,0,0,0,0,1]

fname = 'collected_data/training_data-{}.npy'
fcount = 1

while True:
    fname = fname.format(fcount)

    if os.path.isfile(fname):
        print('File with id ', fcount, 'already exists. Starting a new one.')
        fcount += 1
    else:
        print('No old data files!')
        break

def key_for_nn(keys):

    if 'W' in keys:
        out = forward
    elif 'S' in keys:
        out = reverse
    elif 'A' in keys:
        out = full_left
    elif 'D' in keys:
        out = full_right
    elif 'Q' in keys:
        out = left
    elif 'E' in keys:
        out = right
    elif 'Z' in keys:
        out = r_left
    elif 'X' in keys:
        out = r_right
    else:
        out = no_key
    return out

def collect_data(fname, fcount):
    '''fname = file_name
    starting_value = starting_value'''
    training_data = []
    
    for i in list(range(3))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    
    print('Started!')
    
    while(True):
        
        if not paused:

            screen = get_screen(region=(20,150,975,850))
            screen = cv2.resize(screen, (292,255))
            # run a color convert:
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)
            
            keys = check_key()
            out = key_for_nn(keys)
            training_data.append([screen, out])

            if len(training_data) % 100 == 0:
                print(len(training_data))
                
                if len(training_data) == 500:
                    np.save(fname, training_data)
                    print('Saved data in file ', fname)
                    
                    training_data = []
                    fcount += 1
                    fname = 'training_data-{}.npy'.format(fcount)

                    
        keys = check_key()
        if 'P' in keys:
            if paused:
                paused = False
                print('Resumed data collection!')
                time.sleep(1)
            else:
                print('Paused data collection!')
                paused = True
                time.sleep(1)


collect_data(fname, fcount)
