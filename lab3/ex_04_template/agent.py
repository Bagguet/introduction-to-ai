import random
import numpy as np
from queue import PriorityQueue
import math


class Agent:
    def __init__(self, size, walls, graph, loc, dir, goal):
        self.size = size
        self.walls = walls
        self.graph = graph
        # list of valid locations
        self.locations = list(self.graph.keys())
        # dictionary from location to its index in the list
        self.loc_to_idx = {loc: idx for idx, loc in enumerate(self.locations)}
        self.loc = loc
        self.dir = dir
        self.goal = goal

        self.path = self.find_path()

    def __call__(self):
        action = self.loc

        # select action to reach first location in self.path
        # TODO PUT YOUR CODE HERE



        # ------------------

        return action
    def djikstra_modified(self, s, g):
        nodes = self.graph
        visited = set()
        # słownik kosztów
        cost = {n: float('inf') for n in nodes}
        # słownik poprzedników
        parent = {n: None for n in nodes}
        # utwórz kolejke, w której elementy są ułożone nie w kolejności wprowadzania, lecz w kolejności priorytetu.
        q = PriorityQueue()
        # dodaj wierzchołek startowy
        q.put((0, s))
        cost[s] = 0
        # dopóki kolejka nie jest pusta, czyli są jeszcze jakieś wierzchołki do odwiedzenia
        while not q.empty():
            # pobierz wierzchołek o najmniejszym priotytecie i usuń go z kolejki
            cur_n = q.get()[1]
            # przerwij jeśli odwiedzony
            if cur_n in visited:
                continue
            # dodaj wierzchołek do listy odwiedonych
            visited.add(cur_n)
            # przerwij jeśli dotarliśmy do celu
            if cur_n == g:
                break
            # dla wszystkich krawędzi z aktualnego wierzchołka    
            for nh in nodes[cur_n]: 
                # przerwij jeśli sąsiad był już odwiedzony
                #print(nh)
                #print(cost[cur_n])
                if nh in visited:
                    continue  
                # pobierz koszt sąsiada lub przypisz mu inf
                old_cost = cost[nh]
                # oblicz koszt dla danego wierzchołka
                x,y = cur_n
                x1,y1 = nh  
                distance = math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
                new_cost = cost[cur_n] + distance
                #print(new_cost)

                # rozważ nową ścieżkę tylko wtedy, gdy jest lepsza niż dotychczas najlepsze ścieżka
                if new_cost < old_cost:
                    # zaktualizuj wartość sąsiada w słowniku kosztów
                    cost[nh] = new_cost
                    # ustaw poprzednika
                    parent[nh] = cur_n
                    # dodaj sąsiada do kolejki
                    q.put((new_cost, nh))
        # odtwórz ścieżkę
        path = []
        cur_n = g
        while cur_n is not None:
            path.append(cur_n)
            cur_n = parent[cur_n]
        path.reverse()
        print(path)
        return path
    def find_path(self):
        path = []

        # find path from sel.loc to self.goal
        # TODO PUT YOUR CODE HERE
        s = self.loc    
        g = self.goal
        path = self.djikstra_modified(s, g)
        
        
        
        # ------------------

        return path

    def get_path(self):
        return self.path
