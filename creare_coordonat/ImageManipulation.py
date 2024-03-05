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
        self._face_one.speed_points.append([500, 500])
        self._face_two.points = self._face_one.points.copy()
        self._face_two.speed_points.append([500, 500])
        
    def draw_points_on_img(self, points_positions:dict, points_speeds:list, window_name:list, *image_copy):
        
        #positions
        for i, k in enumerate(points_positions):
            point = points_positions.get(k)
            x = point[0]
            y = point[1]
            color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)

            cv2.circle(image_copy[0], (x, y), 8, color, -1)
            cv2.imshow(window_name[0], image_copy[0])
            
            cv2.circle(image_copy[1], (x, y), 8, color, -1)
            cv2.imshow(window_name[1], image_copy[1])
            
        #speeds
        color = (255, 0, 0)
        for elem in points_speeds:
            x = elem[0]
            y = elem[1]
            cv2.circle(image_copy[0], (x, y), 3, color, -1)
            cv2.imshow(window_name[0], image_copy[0])
            
            cv2.circle(image_copy[1], (x, y), 3, color, -1)
            cv2.imshow(window_name[1], image_copy[1])
            
        
    def draw_points_logic(self):
        image1_copy = self._face_one.image.copy()
        image2_copy = self._face_two.image.copy()
        image_start_copy = self._face_start.image.copy()
        image_end_copy = self._face_end.image.copy()
        
        if self.update_only_second == False:
            self.draw_points_on_img(self._face_one.points, self._face_one.speed_points, [self._face_one.window_name, self._face_start.window_name],image1_copy, image_start_copy)
            self.draw_points_on_img(self._face_two.points, self._face_two.speed_points, [self._face_two.window_name, self._face_end.window_name],image2_copy, image_end_copy)

        elif self.update_only_second:
            self.draw_points_on_img(self._face_two.points, self._face_two.speed_points, [self._face_two.window_name, self._face_end.window_name],image2_copy, image_end_copy)


    # def update_points_positions(self, mouse_x, mouse_y, point_positions:dict, point_speeds:list):
    #     key = "p" + str(self.selected_point_index)
    #     time = point_positions.get(key)[2]
    #     # positionx_before = point_positions.get(key)[0]
    #     # positiony_before = point_positions.get(key)[1]
    #     point_speeds[self.selected_point_index][0] = (point_speeds[self.selected_point_index][0] - point_positions.get(key)[0]) + mouse_x
    #     point_speeds[self.selected_point_index][1] = (point_speeds[self.selected_point_index][1] - point_positions.get(key)[1]) + mouse_y
    #     point_positions.update({key: (mouse_x, mouse_y, time)})
        
    #     print(point_positions.get(key), point_speeds[self.selected_point_index])

    # def update_points_positions(self, mouse_x, mouse_y, point_positions: dict, point_speeds: list):
    #     key = "p" + str(self.selected_point_index)
    #     time = point_positions.get(key)[2]

    #     if self.update_only_second is False:
    #         point_positions.update({key: (mouse_x, mouse_y, time)})
    #         self._face_two.points[key] = (mouse_x, mouse_y, time)
    #         self._face_two.speed_points[self.selected_point_index][0] = mouse_x
    #         self._face_two.speed_points[self.selected_point_index][1] = mouse_y
    #         print(point_positions.get(key), self._face_one.speed_points[self.selected_point_index])

    #     elif self.update_only_second:
    #         point_positions.update({key: (mouse_x, mouse_y, time)})
    #         self._face_one.points[key] = (mouse_x, mouse_y, time)  # Update points for _face_one
    #         self._face_one.speed_points[self.selected_point_index][0] = mouse_x
    #         self._face_one.speed_points[self.selected_point_index][1] = mouse_y
    #         print(point_positions.get(key), self._face_two.speed_points[self.selected_point_index])

    #     point_speeds[self.selected_point_index][0] = mouse_x
    #     point_speeds[self.selected_point_index][1] = mouse_y
    
    
    def update_points_positions(self, mouse_x, mouse_y, point_positions: dict, point_speeds: list):
        key = "p" + str(self.selected_point_index)
        time = point_positions.get(key)[2]

        if self.update_only_second is False:
            point_positions.update({key: (mouse_x, mouse_y, time)})
            self._face_two.points[key] = (mouse_x, mouse_y, time)
            self._face_two.speed_points[self.selected_point_index][0] = mouse_x
            self._face_two.speed_points[self.selected_point_index][1] = mouse_y
            print(point_positions.get(key), self._face_one.speed_points[self.selected_point_index])

        elif self.update_only_second:
            point_positions.update({key: (mouse_x, mouse_y, time)})
            print(point_positions.get(key), self._face_two.speed_points[self.selected_point_index])

        point_speeds[self.selected_point_index][0] = mouse_x
        point_speeds[self.selected_point_index][1] = mouse_y
   
    def update_points_speeds(self, mouse_x, mouse_y, *points_speeds):

        for elem in points_speeds:
            elem[self.selected_point_index][0] = mouse_x
            elem[self.selected_point_index][1] = mouse_y            

    def update_speeds(self, speed_points:list, position_points:dict, face_identifier:int):
        if self.speed_movement_button.config('text')[-1] == 'Move speeds':
            
            returned_speed = []
            for i, k in enumerate(position_points):
                point = position_points.get(k)
                # print(point, type(point))
                if face_identifier == 1:
                    # print(speed_points[0], speed_points[1], type(speed_points[0]), type(speed_points[1]))
                    returned_speed.append(
                        math.sqrt(
                                pow((point[0] - speed_points[i][0]), 2) + pow((point[1] - speed_points[i][1]), 2)
                        )
                    )
                    # print(returned_speed[i])
                elif face_identifier == 2:
                    returned_speed.append(
                        math.sqrt(
                                pow((point[0] - speed_points[i][0]), 2) + pow((point[1] - speed_points[i][1]), 2)
                        )
                    )
            # print(returned_speed)
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
            for i,elem in enumerate(point):
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

        # elif event == cv2.EVENT_LBUTTONDOWN and param == self._face_two.window_name:
            
        #     if self.speed_movement_button.config('text')[-1] == 'Move points':
        #         self.verify_button_down(mouse_x, mouse_y, self._face_two.points)
                
        #     elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
        #         self.verify_button_down(mouse_x, mouse_y, self._face_two._speed_points)
        #     self.update_only_second = True
        elif event == cv2.EVENT_LBUTTONDOWN and param == self._face_two.window_name:
            if self.speed_movement_button.config('text')[-1] == 'Move points':
                self.verify_button_down(mouse_x, mouse_y, self._face_two.points)
            elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                self.verify_button_down(mouse_x, mouse_y, self._face_two._speed_points)
            self.update_only_second = True
            
        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None

        # elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
        #     if self.update_only_second is False:
        #         if self.speed_movement_button.config('text')[-1] == 'Move points':
        #             self.update_points_positions(mouse_x, mouse_y, self._face_one.points, self._face_one.speed_points)
        #             self._face_two.points = self._face_one.points.copy()
        #             self.update_speeds(self._face_two.speed_points, self._face_two.points, 1)
        #         # elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
        #         #     self.update_speeds(self._face_one.speed_points, self._face_one.points, 1)
        #         #     self._face_two.speed_points = self._face_one.speed_points.copy()
        #         #     print(self._face_two.speed_points)
        #     elif self.update_only_second:
        #         if self.speed_movement_button.config('text')[-1] == 'Move points':
        #             self.update_points_positions(mouse_x, mouse_y, self._face_two.points, self._face_two.speed_points)
        #             self.update_speeds(self._face_two.speed_points, self._face_two.points, 2)
        
        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            if self.update_only_second is False:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points_positions(mouse_x, mouse_y, self._face_one.points, self._face_one.speed_points)
                    self._face_two.points = self._face_one.points.copy()
                    self.update_speeds(self._face_two.speed_points, self._face_two.points, 1)
                    
                elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                    # self.update_points_speeds(mouse_x, mouse_y)
                    self.update_points_speeds(mouse_x, mouse_y, self._face_one.speed_points, self._face_two.speed_points)
                    
            elif self.update_only_second:
                if self.speed_movement_button.config('text')[-1] == 'Move points':
                    self.update_points_positions(mouse_x, mouse_y, self._face_two.points, self._face_two.speed_points)
                    self.update_speeds(self._face_two.speed_points, self._face_two.points, 2)
                    
                elif self.speed_movement_button.config('text')[-1] == 'Move speeds':
                    # self.update_points_speeds(mouse_x, mouse_y)
                    self.update_points_speeds(mouse_x, mouse_y, self._face_two.speed_points)
       
        
        self.draw_points_logic()
        
