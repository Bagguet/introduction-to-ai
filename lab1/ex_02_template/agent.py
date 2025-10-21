import random
from queue import Queue
import numpy as np

from gridutil import generate_locations


class Agent:
    def __init__(self, size, walls, loc, dir, goal):
        self.size = size
        self.walls = walls
        # list of valid locations
        self.locations = list({*generate_locations(self.size)}.difference(self.walls))
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal
        self.graph = self.locations_to_graph()
        self.path = self.find_path()
        self.actual_step = 0

    def __call__(self):
        
        action = 'N'
        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE
        path = self.path
        
        step = path[self.actual_step]
        if step[0] > self.loc[0]:
            action = 'E'
            self.loc = step
            self.dir = 'E'
        elif step[0] < self.loc[0]:
            action = 'W'
            self.loc = step
            self.dir = 'W'
        elif step[1] < self.loc[1]:
            action = 'S'
            self.loc = step
            self.dir = 'S'
        elif step[1] > self.loc[1]:
            action = 'N'
            self.loc = step
            self.dir = 'N'
        self.actual_step += 1
        # ------------------

        return action

    def locations_to_graph(self):
        graph = {}
        self.locations.sort(key=lambda x: x[0])
        for loc in self.locations:
            if loc not in graph:
                graph[loc] = []
            if loc[0] > 0 and (loc[0] - 1, loc[1]) not in self.walls:
                graph[loc].append((loc[0] - 1, loc[1]))
            if loc[0] < self.size - 1 and (loc[0] + 1, loc[1]) not in self.walls:
                graph[loc].append((loc[0] + 1, loc[1]))
            if loc[1] > 0 and (loc[0], loc[1] - 1) not in self.walls:
                graph[loc].append((loc[0], loc[1] - 1))
            if loc[1] < self.size - 1 and (loc[0], loc[1] + 1) not in self.walls:
                graph[loc].append((loc[0], loc[1] + 1))

        return graph

    def find_path(self):
        path = []
        graph = self.locations_to_graph()
        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        visited = set()
        parent = {n: None for n in graph}
        s = self.loc
        g = self.goal

        q = Queue()
        q.put(s)
        parent[s] = s
        while not q.empty():
            cur_n = q.get()
            if cur_n == g:
                break
            for nh in graph[cur_n]:
                if nh not in visited:
                    parent[nh] = cur_n
                    visited.add(nh)
                    q.put(nh)
        path = []
        cur_n = g
        while cur_n != s:
            path.append(cur_n)
            print(cur_n)
            cur_n = parent[cur_n]
        path.reverse()


        # ------------------

        return path

    def get_path(self):
        return self.path
