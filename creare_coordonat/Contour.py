import math

import numpy as np
import cv2
import matplotlib.pyplot as plt

from Face import Face


class Contour:
    def __init__(self, face_one: Face, face_two: Face):
        self._face_one = face_one
        self._face_two = face_two
        # self._points1 = points1
        # self._points2 = points2
        self._speed = []

    @staticmethod
    def line(self, points, image, window_name):
        list_of_polynomial_points = []

        for j in range(len(points) - 1):

            x_p1, y_p1, t_p1 = points['p' + str(j)]
            x_p2, y_p2, t_p2 = points['p' + str(j + 1)]

            for i in range(0, 100, 1):
                i = i / 100

                x = x_p1 + (x_p2 - x_p1) * i
                y = y_p1 + (y_p2 - y_p1) * i
                t = t_p1 + (t_p2 - t_p1) * i
                # print(x, y, t)
                tuple_point = (x, y, t)
                cv2.circle(image,
                           (round(tuple_point[0]), (round(tuple_point[1]))),
                           2, [255, 0, 0], -1
                           )
                list_of_polynomial_points.append(tuple_point)
        # cv2.imshow(window_name, image)
        # self.speed(list_of_polynomial_points)
        #
        # self.plotting(list_of_polynomial_points, image)

    def polynom_draw(self):
        """Primeste data puncte din dictionar si creaza linia."""
        # Create copies of the original images
        image_one_copy = self._face_one.image.copy()
        image_two_copy = self._face_two.image.copy()

        # Draw new lines on the copies
        self.line(self._face_one.points, image_one_copy, self._face_one.window_name)
        self.line(self._face_two.points, image_two_copy, self._face_one.window_name)
        cv2.imshow(self._face_one.window_name, image_one_copy)
        cv2.imshow(self._face_two.window_name, image_two_copy)
        # Update the original images with the copies
        # self._face_one.image[:] = image_one_copy
        # self._face_two.image[:] = image_two_copy
        #
        # self.line(self._points1, self._face_one.image)
        # self.line(self._points2, self._face_two.image)

    def speed(self, list_of_points):
        for i in range(len(list_of_points) - 1):
            speed_x = float(
                (list_of_points[i][0] - list_of_points[i + 1][0]) / (list_of_points[i][2] - list_of_points[i + 1][2]))
            speed_y = float(
                (list_of_points[i][1] - list_of_points[i + 1][1]) / (list_of_points[i][2] - list_of_points[i + 1][2]))
            self._speed.append(math.sqrt(speed_x ** 2 + speed_y ** 2))

    def plotting(self, list_of_polynomial_points, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # plot x si y
        plt.scatter([p[0] for p in list_of_polynomial_points], [p[1] for p in list_of_polynomial_points], color='red')
        plt.imshow(image_rgb)
        plt.title("x si y")
        plt.show()

        # plot t si x
        plt.scatter([p[2] for p in list_of_polynomial_points], [p[0] for p in list_of_polynomial_points], color='red')
        plt.imshow(image_rgb)
        plt.title("t si x")
        plt.show()

        # plot t si y
        plt.scatter([p[2] for p in list_of_polynomial_points], [p[1] for p in list_of_polynomial_points], color='red')
        plt.imshow(image_rgb)
        plt.title("t si y")
        plt.show()

        # plot v si t
        plt.scatter([p[2] for p in list_of_polynomial_points], [p for p in self._speed], color='red')
        plt.imshow(image_rgb)

        plt.title("t si v")
        plt.show()
