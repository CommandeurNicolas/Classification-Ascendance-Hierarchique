from math import *


class Point:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.label} -> x:{self.x} y:{self.y}'

    def __str__(self) -> str:
        return f'{self.label} -> x:{self.x} y:{self.y}'


class Cluster:
    def __init__(self):
        self.data: Point = []

    def add(self, item):
        self.data.append(item)

    def show(self):
        for t in self.data:
            print(t)

    def distnce(self,a, b):
        return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))

    def min(self, item):
        res = 100000000000
        for t in self.data:
            if(self.distnce(t, item) < res):
                res = self.distnce(t, item)
        return res

    def max(self, item):
        res = -1
        for t in self.data:
            if(self.distnce(t, item) > res):
                res = self.distnce(t, item)
        return res
