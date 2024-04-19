import random


class Graph:
    def __init__(self, town):
        self.town = town
        self.connections = []

    class Ant:
        def __init__(self, home):
            self.tabu = []
            self.home = home

        def add_town(self, town):
            self.tabu.append(town)

def probability(smelly, view, total):
    return (smelly * view) / total





