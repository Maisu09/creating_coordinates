import cv2
import tkinter
from tkinter import filedialog
from Contour import Contour
from SysManipulation import SysManipulation
from Face import Face


class ImageManipulation:
    selected_point_index = None

    def __init__(self, points: dict, file_path1, image1, file_path2, image2):

        self._image = cv2.imread(file_path1)
        self._points = points
        self._selected_points_index = None
        self._window_name = 'Move Points with Mouse'

        face_one = Face(image1, file_path1, 'First face')
        face_two = Face(image2, file_path2, 'Second face')

        root = tkinter.Tk()

        cv2.namedWindow(face_one.window_name)
        cv2.imshow(face_one.window_name, face_one.image)
        cv2.setMouseCallback(face_one.window_name, self.on_mouse_event)

        add_button = tkinter.Button(root, text='Add Point', command=self.set_points_list_add)
        add_button.pack()

        polynom_button = tkinter.Button(root, text='Connect Points', command=self.connect_points)
        polynom_button.pack()

        save_choose_button = tkinter.Button(root, text='Save In Different Directory', command=self.save_image)
        save_choose_button.pack()

        # save_automate_button = tkinter.Button(root, text='Auto-save', command=self.automation_save)
        # save_automate_button.pack()

        root.mainloop()
        cv2.destroyAllWindows()

    def connect_points(self):
        contour = Contour(self._image, self._points)
        contour.polynom_draw(self._window_name)

    def set_points_list_add(self):
        position = len(self._points)
        new_key = "p" + str(position)
        self._points[new_key] = [500, 500, self._points["p" + str(position - 1)][2] + 100]

    def update_image(self):
        for i, k in enumerate(self._points):
            values_of_dict = self._points.get(k)
            x = values_of_dict[0]
            y = values_of_dict[1]

            color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)
            cv2.circle(self._image, (x, y), 10, color, -1)

    def automation_save(self):
        """A one click solution saving and generating the line."""
        self.update_image()
        sys_manipulation = SysManipulation()
        sys_manipulation.change_dir_picture()
        sys_manipulation.save_traced_img(self._image, False)

    def save_image(self):
        self.update_image()
        path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if path:
            cv2.imwrite(path, self._image)

        # self.automation_save()

    def draw_points(self):
        image_copy = self._image.copy()

        for i, k in enumerate(self._points):
            values_of_dict = self._points.get(k)
            x = values_of_dict[0]
            y = values_of_dict[1]

            color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)
            cv2.circle(image_copy, (x, y), 10, color, -1)

        cv2.imshow(self._window_name, image_copy)

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
