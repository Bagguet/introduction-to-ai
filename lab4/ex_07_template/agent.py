# prob.py
# This is

import random
import numpy as np
import queue
import math

from gridutil import generate_locations


class Agent:
    def __init__(self, size, walls, loc, dir, eps_move, eps_perc):
        self.size = size
        self.walls = walls
        self.eps_move = eps_move
        self.eps_perc = eps_perc
        # list of valid locations
        self.locations = list({*generate_locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.action_dir = 1

        self.t = 0
        self.P = np.zeros(self.size, dtype=float)
        # we start from 0
        self.P[loc[0]] = 1.0

    def __call__(self):
        # most probable location
        loc = np.argmax(self.P)
        # if reached one of the ends then start moving in the opposite direction
        if (self.action_dir == 1 and loc == self.size - 1) or \
           (self.action_dir == -1 and loc == 0):
            self.action_dir *= -1

        # move by one or two cells
        action = self.action_dir * np.random.choice([1, 2])

        # use information about requested action to update posterior
        # TODO PUT YOUR CODE HERE
        self.predict_posterior(action)
        self.correct_posterior(self.loc)


        # ------------------

        return action
    def randomizer(self, error):
        probs =  {
            0: 1-6*error,
            1: error*2,
            -1: error*2,
            2: error,
            -2: error,
        }
        number = list(probs.keys())
        probabilities = list(probs.values())
        return np.random.choice(number, p=probabilities)
    
    def predict_posterior(self, action):
        # predict posterior using requested action
        # TODO PUT YOUR CODE HERE
        action = action + self.randomizer(self.eps_move)
        # ------------------

        return action

    def correct_posterior(self, percept):
        # TODO PUT YOUR CODE HERE
        # correct posterior using measurements
        percept = percept + self.randomizer(self.eps_perc)
        # ------------------
        return percept

    def get_posterior(self):
        return self.P
