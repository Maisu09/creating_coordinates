import cv2
import tkinter
from tkinter import filedialog
from Contour import Contour
from SysManipulation import SysManipulation
from Face import Face


class Image_manipulation:
    def __init__(self, points: dict, file_path1, image1, file_path2, image2):
        self._points = points
        self._face_one = Face(file_path1, image1, 'First face')
        self._face_two = Face(file_path2, image2, 'Second face')
        root = tkinter.Tk()

        cv2.namedWindow(self._face_one.window_name)
        cv2.imshow(self._face_one.window_name, self._face_one.image)
        cv2.imshow(self._face_two.window_name, self._face_two.image)
        cv2.setMouseCallback(self._face_one.window_name, self.on_mouse_event)

    def draw_points_second_img(self):
        pass

    def draw_points(self):


    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, k in enumerate(self._points):

                values_of_dict = self._points.get(k)
                x = values_of_dict[0]
                y = values_of_dict[1]

                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i

        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None

            # verificare modificare puncte in dict
            # for i, key in enumerate(self.points):
            #     print(key, self.points.get(key))
            # print('\n')

        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            key = "p" + str(self.selected_point_index)
            time = self._points.get(key)[2]
            self._points.update({key: (mouse_x, mouse_y, time)})

        self.draw_points()
