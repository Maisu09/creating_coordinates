import cv2
import tkinter
from tkinter import filedialog
from Contour import Contour
from SysManipulation import SysManipulation
from Face import Face
import math
# vitezele is calculte ca si dif intre punc alastru care  e varf ves\ctor si punctu de poz. trebe sa fie initial suprapuse si dupa sa le pot muta

class ImageManipulation:
    def __init__(self, points1: dict, file_path1, image1, file_path2, image2):
        self.selected_point_index = None
        self.update_only_second = False

        self._face_one = Face(file_path1, image1, 'First face', points1)
        self._face_two = Face(file_path2, image2, 'Second face', self._face_one.points.copy())
        self._face_start = Face(file_path1, image1, 'Starting face', self._face_one.points)
        self._face_end = Face(file_path2, image2, 'Ending face', self._face_two.points)

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
        
                
        self._speeds_face_one = self.update_speeds(self._face_one.speed_points, self._face_one.points, 1)
        self._speeds_face_two = self.update_speeds(self._face_two.speed_points, self._face_two.points, 2)

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
        
            for elem in self._face_one.speed_points:
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
            for elem in self._face_two.speed_points:
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

    def update_points(self, mouse_x, mouse_y, point_positions:dict, point_speeds:list):
        key = "p" + str(self.selected_point_index)
        time = point_positions.get(key)[2]
        # positionx_before = point_positions.get(key)[0]
        # positiony_before = point_positions.get(key)[1]
        point_speeds[self.selected_point_index][0] = (point_speeds[self.selected_point_index][0] - point_positions.get(key)[0]) + mouse_x
        point_speeds[self.selected_point_index][1] = (point_speeds[self.selected_point_index][1] - point_positions.get(key)[1]) + mouse_y
        point_positions.update({key: (mouse_x, mouse_y, time)})
        
        print(point_positions.get(key), point_speeds[self.selected_point_index])

    def update_speeds(self, speed_points:list, position_points:dict, face_identifier:int):
        if self.speed_movement_button.config('text')[-1] == 'Move speeds':
            # Calculate speeds as the difference between the positions
            returned_speed = []
            for i, k in enumerate(position_points):
                point = position_points.get(k)
                print(point, type(point))
                if face_identifier == 1:
                    # print(speed_points[0], speed_points[1], type(speed_points[0]), type(speed_points[1]))
                    returned_speed.append(
                        math.sqrt(
                                pow((point[0] - speed_points[i][0]), 2) + pow((point[1] - speed_points[i][1]), 2)
                        )
                    )
                    print(returned_speed[i])
                elif face_identifier == 2:
                    returned_speed.append(
                        math.sqrt(
                                pow((point[0] - speed_points[i][0]), 2) + pow((point[1] - speed_points[i][1]), 2)
                        )
                    )
            print(returned_speed)
            return speed_points
                    
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
            for i, elem in enumerate(point):
                x = elem[0]
                y = elem[1]
                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i
                    break
                
    
    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        
        if event == cv2.EVENT_LBUTTONDOWN and param == self._face_one.window_name:
            
            if self.speed_movement_button.config('text')[-1] == 'Move points':
                self.verify_button_down(mouse_x, mouse_y, self._face_one.points)
                
            elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                self.verify_button_down(mouse_x, mouse_y, self._face_one._speed_points)
                
            # print("primul")
            self.update_only_second = False

        elif event == cv2.EVENT_LBUTTONDOWN and param == self._face_two.window_name:
            
            if self.speed_movement_button.config('text')[-1] == 'Move points':
                self.verify_button_down(mouse_x, mouse_y, self._face_two.points)
                
            elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                self.verify_button_down(mouse_x, mouse_y, self._face_two._speed_points)
            self.update_only_second = True

        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None

        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            if self.update_only_second is False:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points(mouse_x, mouse_y, self._face_one.points, self._face_one.speed_points)
                    self._face_two.points = self._face_one.points.copy()
                    self.update_speeds(self._face_two.speed_points, self._face_two.points, 1)
                # elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                #     self.update_speeds(self._face_one.speed_points, self._face_one.points, 1)
                #     self._face_two.speed_points = self._face_one.speed_points.copy()
                #     print(self._face_two.speed_points)
            elif self.update_only_second:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points(mouse_x, mouse_y, self._face_two.points, self._face_two.speed_points)
                    self.update_speeds(self._face_two.speed_points, self._face_two.points, 2)
        self.draw_points()
