import numpy as np
import cv2


class Contour:
    def __init__(self):
        # self.number = [4, 3, 2, 1] #4x**3+3x**2+2x+1
        self.polynom = []
        self.m = 0

    @staticmethod
    def gradient(distance):
        """Realizeaza panta ecuatiei bazate pe cele doua puncte."""
        return (distance[0][0] + distance[1][0]) / (distance[0][1] + distance[1][1])

    def polynom_draw(self, two_given_points: list, image_copy, window_name):
        """Primeste doua puncte din dictionar si creaza linia."""
        if two_given_points[0][0] > two_given_points[1][0]:
            two_given_points.reverse()
        self.m = self.gradient(two_given_points)

        x_values = np.linspace(two_given_points[0][0], two_given_points[1][0])

        y_values = 3 * x_values + 5

        for x, y in zip(x_values, y_values):
            if x < two_given_points[1][0]:
                cv2.circle(image_copy, (x, y), 2, (0, 255, 0))
        cv2.imshow(window_name, image_copy)
