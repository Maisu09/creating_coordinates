import cv2
import tkinter
from tkinter import filedialog
from Contour import Contour
from SysManipulation import SysManipulation
from Face import Face
# vitezele is calculte ca si dif intre punc alastru care  e varf ves\ctor si punctu de poz. trebe sa fie initial suprapuse si dupa sa le pot muta

class ImageManipulation:
    def __init__(self, points1: dict, file_path1, image1, file_path2, image2):
        self.selected_point_index = None
        self.update_only_second = False

        self._face_one = Face(file_path1, image1, 'First face', points1)
        self._face_two = Face(file_path2, image2, 'Second face', self._face_one.points.copy())
        self._face_start = Face(file_path1, image1, 'Starting face', self._face_one.points)
        self._face_end = Face(file_path2, image2, 'Ending face', self._face_two.points)
        
        self._speeds = self.setSpeeds(self._face_one.points)
        root = tkinter.Tk()

        # cv2.namedWindow(self._face_one.window_name)
        cv2.imshow(self._face_one.window_name, self._face_one.image)
        cv2.imshow(self._face_two.window_name, self._face_two.image)
        cv2.imshow(self._face_start.window_name, self._face_start.image)
        cv2.imshow(self._face_end.window_name, self._face_end.image)

        cv2.setMouseCallback(self._face_one.window_name, self.on_mouse_event, self._face_one.window_name)
        cv2.setMouseCallback(self._face_two.window_name, self.on_mouse_event, self._face_two.window_name)

        add_point_button = tkinter.Button(root, text='Add point', command=self.add_point)
        add_point_button.pack()
        
        polynom_button = tkinter.Button(root, text='Connect Points', command=self.connect_points)
        polynom_button.pack()
        
        self.speed_movement_button = tkinter.Button(root, text='Move speeds', command=self.switch)
        self.speed_movement_button.pack()
   
    def setSpeeds(self, points:dict):
        list_points = [] 
        for i,k in enumerate(points):
            elems = points.get(k)
            list_points.append([elems[0], elems[1]])
        print(list_points)
        
        speed = []
        for x, y in list_points:
            speed.append([x, y])        
        return speed

    def switch(self):
        if self.speed_movement_button.config('text')[-1] == 'Move points':
            self.speed_movement_button.config(text='Move speeds')
            print(self.speed_movement_button.config('text')[-1])
        else:
            self.speed_movement_button.config(text='Move points')
            print(self.speed_movement_button.config("text")[-1])

    def connect_points(self):
        contour = Contour(self._face_one, self._face_two)
        contour.polynom_draw()

    def add_point(self):
        position = len(self._face_one.points)
        new_key = 'p' + str(position)
        self._face_one.points[new_key] = [500, 500, self._face_one.points['p' + str(position - 1)][2] + 100]
        self._face_two.points = self._face_one.points.copy()

    def draw_move_points(self, *image_copy):
        # pozitii
        if self.update_only_second is False:
            for i, k in enumerate(self._face_one.points):
                values_of_dict = self._face_one.points.get(k)
                x_p1 = values_of_dict[0]
                y_p1 = values_of_dict[1]

                values_of_dict = self._face_two.points.get(k)
                x_p2 = values_of_dict[0]
                y_p2 = values_of_dict[1]

                color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)

                for j in range(len(image_copy)):
                    if j % 2 == 0:
                        cv2.circle(image_copy[j], (x_p1, y_p1), 8, color, -1)
                        cv2.imshow(self._face_one.window_name if j == 0 else self._face_start.window_name,
                                   image_copy[j])
                    else:
                        cv2.circle(image_copy[j], (x_p2, y_p2), 8, color, -1)
                        cv2.imshow(self._face_two.window_name if j == 1 else self._face_end.window_name,
                                   image_copy[j])
            #viteze
            color = (255, 0, 0)
        
            for elem in self._speeds:
                for j in range(len(image_copy)):
                    if j % 2 == 0:
                        cv2.circle(image_copy[j], (elem[0], elem[1]), 5, color, -1)
                        cv2.imshow(self._face_one.window_name if j == 0 else self._face_start.window_name,
                                   image_copy[j])
                    else:
                        cv2.circle(image_copy[j], (elem[0], elem[1]), 5, color, -1)
                        cv2.imshow(self._face_two.window_name if j == 1 else self._face_end.window_name,
                                   image_copy[j])

        elif self.update_only_second is True:
            #pozitii
            for i, k in enumerate(self._face_two.points):
                values_of_dict = self._face_two.points.get(k)
                x = values_of_dict[0]
                y = values_of_dict[1]

                color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)

                cv2.circle(image_copy[1], (x, y), 8, color, -1)
                cv2.circle(image_copy[3], (x, y), 8, color, -1)

            cv2.imshow(self._face_two.window_name, image_copy[1])
            cv2.imshow(self._face_end.window_name, image_copy[3])
            #viteze
            color = (255, 0, 0)
            for elem in self._speeds:
                for j in range(len(image_copy)):
                    if j % 2 == 0:
                        cv2.circle(image_copy[j], (elem[0], elem[1]), 5, color, -1)
                        cv2.imshow(self._face_one.window_name if j == 0 else self._face_start.window_name,
                                    image_copy[j])
                    else:
                        cv2.circle(image_copy[j], (elem[0], elem[1]), 5, color, -1)
                        cv2.imshow(self._face_two.window_name if j == 1 else self._face_end.window_name,
                                    image_copy[j])

    def draw_points(self):
        image1_copy = self._face_one.image.copy()
        image2_copy = self._face_two.image.copy()
        image_start_copy = self._face_start.image.copy()
        image_end_copy = self._face_end.image.copy()

        # self.draw_move_points(self._face_one.image, self._face_two.image)
        # if self.speed_movement_button.config('text')[-1] == 'Move points':
        self.draw_move_points(image1_copy, image2_copy, image_start_copy, image_end_copy)
        # else:
        #     self.draw_move_speeds(image1_copy, image2_copy, image_start_copy, image_end_copy)

    def update_points(self, mouse_x, mouse_y, point):
        key = "p" + str(self.selected_point_index)
        time = point.get(key)[2]
        point.update({key: (mouse_x, mouse_y, time)})

    def update_speeds(self):
        if self.speed_movement_button.config('text')[-1] == 'Move speeds':
            # Calculate speeds as the difference between the positions
            self._speeds = []
            for key in self._face_one.points:
                x_p1, y_p1 = self._face_one.points[key][:2]
                x_p2, y_p2 = self._face_two.points[key][:2]
                speed_x = x_p2 - x_p1
                speed_y = y_p2 - y_p1
                self._speeds.append([speed_x, speed_y])
    def verify_button_down(self, mouse_x, mouse_y, point):
        
        if self.speed_movement_button.config('text')[-1] == 'Move points':
            for i, k in enumerate(point):
                values_of_dict = point.get(k)
                x = values_of_dict[0]
                y = values_of_dict[1]

                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i
                    break
                
        elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
            for i, elem in enumerate(self._speeds):
                x = elem[0]
                y = elem[1]
                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i
                    break
                
    
    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        if event == cv2.EVENT_LBUTTONDOWN and param == self._face_one.window_name:
            # self.verify_button_down(mouse_x, mouse_y, self._points1)
            if self.speed_movement_button.config('text')[-1] == 'Move points':
                self.verify_button_down(mouse_x, mouse_y, self._face_one.points)
            elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                self.verify_button_down(mouse_x, mouse_y, self._speeds)
                
            # print("primul")
            self.update_only_second = False

        elif event == cv2.EVENT_LBUTTONDOWN and param == self._face_two.window_name:
            # self.verify_button_down(mouse_x, mouse_y, self._points2)
            # if self.speed_movement_button.config('text')[-1] == 'Move points':
            self.verify_button_down(mouse_x, mouse_y, self._face_two.points)
            # print("al doilea")
            # else:
            #     pass
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
            # for i, key in enumerate(self._points1):
            #     print(key, self._points1.get(key))
            # print('\n')
            # for i, key in enumerate(self._points2):
            #     print(key, self._points2.get(key))
            # print('\n')
            # for i, key in enumerate(self._face_one.points):
            #     print(key, self._face_one.points.get(key))
            # print('\n')
            # for i, key in enumerate(self._face_two.points):
            #     print(key, self._face_two.points.get(key))
            # print('\n')

        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            if self.update_only_second is False:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points(mouse_x, mouse_y, self._face_one.points)
                    self._face_two.points = self._face_one.points.copy()
                elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                    self.update_speeds()
            elif self.update_only_second:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points(mouse_x, mouse_y, self._face_two.points)
                    self.update_speeds()
        self.draw_points()
