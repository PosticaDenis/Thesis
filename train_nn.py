# -*- coding: utf-8 -*-
"""
Created on Wed May 23 08:44:53 2018

@author: denis
"""

import numpy as np
from alexnet import alexnet

WIDTH = 90
HEIGHT = 80

LR = 1e-3  # learning rate

EPOCHS = 10

MODEL_NAME = 'models/autonomous-car-{}-{}-{}-epochs-50K-data.model'.format(LR, 'alexnet', EPOCHS)

data_fname  = 'collected_data/training_data-{}.npy'

model = alexnet(WIDTH, HEIGHT, LR)

data_files = 10
for i in range(EPOCHS):
    for i in range(1, data_files + 1):
        train_data = np.load(data_fname.format(i))

        train = train_data[:-250]
        test = train_data[-250:]

        X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
        Y = [i[1] for i in train]

        test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
        test_y = [i[1] for i in test]

        model.fit({'input': X}, {'targets': Y}, n_epoch = 1, validation_set = ({'input': test_x}, {'targets': test_y}), 
            snapshot_step = 500, show_metric = True, run_id = MODEL_NAME)

        model.save(MODEL_NAME)
        print('Saved model.')


# tensorboard --logdir=foo:C:/path/to/log
        
