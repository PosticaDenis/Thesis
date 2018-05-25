# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:44:53 2018

@author: denis
"""

import numpy as np
# from alexnet import alexnet
from models import inception_v3 as googlenet
from random import shuffle

WIDTH = 90
HEIGHT = 80

LR = 1e-3  # learning rate

EPOCHS = 10

MODEL_NAME = ''
PREV_MODEL = ''

data_fname  = 'collected_data/training_data-{}.npy'

model = googlenet(WIDTH, HEIGHT, 1, LR, output = 6, model_name=MODEL_NAME)

data_files = 10
for i in range(EPOCHS):
    data = [i for i in range(1, data_files + 1)]
    shuffle(data)
    for cnt, i in enumerate(data):
        try:
            train_data = np.load(data_fname.format(i))
            
            print('Loaded train data ', data_fname.format(i), ', size ', len(train_data))

            train = train_data[:-50]
            test = train_data[-50:]

            X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
            Y = [i[1] for i in train]

            test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
            test_y = [i[1] for i in test]

            model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}), 
                snapshot_step = 500, show_metric = True, run_id = MODEL_NAME)

            if cnt%10 == 0:
                model.save(MODEL_NAME)
                print('Saved model.')
        except Exception as e:
            print(str(e))


# tensorboard --logdir=foo:C:/path/to/log
        
