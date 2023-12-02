import numpy as np
import cv2
import matplotlib.pyplot as plt


class Contour:
    def __init__(self, image):
        self.image = image

    def polynom_draw(self, points: dict, window_name):
        """Primeste doua puncte din dictionar si creaza linia."""
        list_of_polynomial_points = []
        x_p1, y_p1 = points['p1']
        x_p2, y_p2 = points['p2']

        for i in range(0, 100, 1):
            i = i / 100

            x = x_p1 + (x_p2 - x_p1) * i
            y = y_p1 + (y_p2 - y_p1) * i

            tuple_point = (x, y)
            list_of_polynomial_points.append(tuple_point)

        image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        plt.scatter([p[0] for p in list_of_polynomial_points], [p[1] for p in list_of_polynomial_points], color='red')
        plt.imshow(image_rgb)
        plt.title(window_name)
        plt.show()
