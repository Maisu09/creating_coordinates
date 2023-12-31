import cv2
import tkinter
from tkinter import filedialog
from Contour import Contour
from SysManipulation import SysManipulation
from Face import Face


class Image_manipulation:

    def __init__(self, points1: dict, file_path1, image1, file_path2, image2, points2: dict):
        self.selected_point_index = None
        self.update_only_second = False
        self._points1 = points1
        self._points2 = self._points1.copy()
        self._face_one = Face(file_path1, image1, 'First face')
        self._face_two = Face(file_path2, image2, 'Second face')
        root = tkinter.Tk()

        cv2.namedWindow(self._face_one.window_name)
        cv2.imshow(self._face_one.window_name, self._face_one.image)
        cv2.imshow(self._face_two.window_name, self._face_two.image)

        cv2.setMouseCallback(self._face_one.window_name, self.on_mouse_event, self._face_one.window_name)
        cv2.setMouseCallback(self._face_two.window_name, self.on_mouse_event, self._face_two.window_name)

        add_point_button = tkinter.Button(root, text='Add point', command=self.add_point)
        add_point_button.pack()
        polynom_button = tkinter.Button(root, text='Connect Points', command=self.connect_points)
        polynom_button.pack()

    def connect_points(self):
        contour = Contour(self._face_one, self._points1, self._face_two, self._points2)
        contour.polynom_draw()

    def add_point(self):
        position = len(self._points1)
        new_key = 'p' + str(position)
        self._points1[new_key] = [500, 500, self._points1['p' + str(position - 1)][2] + 100]
        self._points2 = self._points1.copy()

    def draw_function(self, *image_copy):
        if self.update_only_second is False:
            for i, k in enumerate(self._points1):
                values_of_dict = self._points1.get(k)
                x_p1 = values_of_dict[0]
                y_p1 = values_of_dict[1]

                values_of_dict = self._points2.get(k)
                x_p2 = values_of_dict[0]
                y_p2 = values_of_dict[1]
                color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)

                cv2.circle(image_copy[0], (x_p1, y_p1), 10, color, -1)
                cv2.circle(image_copy[1], (x_p2, y_p2), 10, color, -1)

            cv2.imshow(self._face_one.window_name, image_copy[0])
            cv2.imshow(self._face_two.window_name, image_copy[1])

        elif self.update_only_second is True:
            for i, k in enumerate(self._points2):
                values_of_dict = self._points2.get(k)
                x = values_of_dict[0]
                y = values_of_dict[1]

                color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)

                cv2.circle(image_copy[1], (x, y), 10, color, -1)

            cv2.imshow(self._face_two.window_name, image_copy[1])

    def draw_points(self):
        image1_copy = self._face_one.image.copy()
        image2_copy = self._face_two.image.copy()
        # self.draw_function(self._face_one.image, self._face_two.image)
        self.draw_function(image1_copy, image2_copy)

    def update_points(self, mouse_x, mouse_y, point):
        key = "p" + str(self.selected_point_index)
        time = point.get(key)[2]
        point.update({key: (mouse_x, mouse_y, time)})

    def verify_button_down(self, mouse_x, mouse_y, point):
        for i, k in enumerate(point):
            values_of_dict = point.get(k)
            x = values_of_dict[0]
            y = values_of_dict[1]

            if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                self.selected_point_index = i
                break

    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        if event == cv2.EVENT_LBUTTONDOWN and param == self._face_one.window_name:
            self.verify_button_down(mouse_x, mouse_y, self._points1)
            print("primul")
            self.update_only_second = False

        elif event == cv2.EVENT_LBUTTONDOWN and param == self._face_two.window_name:
            self.verify_button_down(mouse_x, mouse_y, self._points2)
            print("al doilea")
            self.update_only_second = True

            # for i, k in enumerate(self._points1):
            #     # print(param)
            #     values_of_dict = self._points1.get(k)
            #     x = values_of_dict[0]
            #     y = values_of_dict[1]
            #
            #     if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
            #         self.selected_point_index = i

        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None
            # verificare modificare puncte in dict
            for i, key in enumerate(self._points1):
                print(key, self._points1.get(key))
            print('\n')
            for i, key in enumerate(self._points2):
                print(key, self._points2.get(key))
            print('\n')

        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            if self.update_only_second is False:
                self.update_points(mouse_x, mouse_y, self._points1)
                self._points2 = self._points1.copy()

            elif self.update_only_second:
                self.update_points(mouse_x, mouse_y, self._points2)

        self.draw_points()
