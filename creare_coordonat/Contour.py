import numpy as np


class Contour:
    def __init__(self):
        # self.number = [4, 3, 2, 1] #4x**3+3x**2+2x+1
        self.polynom = []
        self.m = 0

    @staticmethod
    def gradient(distance):
        return (distance[0][0] + distance[1][0]) / (distance[0][1] + distance[1][1])

    def polynom_draw(self, two_given_points):
        self.m = self.gradient(two_given_points)
