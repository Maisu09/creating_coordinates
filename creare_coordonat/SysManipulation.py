import os
import cv2


class SysManipulation:

    @staticmethod
    def create_folder_in_dir(folder_name:str):
        """ Changing wd to the directory where images are stored. """
        if os.getcwd() != r'C:\Users\mflor\Desktop\Licenta':
            os.chdir(r'C:\Users\mflor\Desktop\Licenta')
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print('folder exist')
            
        os.chdir(folder_name)
        print(os.getcwd())
        
        
    @staticmethod
    def save_points(points:dict, name:str, speeds:list):
        """  """
        ## primeste puncte schimba directoru in ala creat face dupa un fisier in care salveaza cu open punctele din image man.
        name.strip()
        name = name +'.txt'
        with open(name, 'w') as file:
            # file.write('x          y \n')
            
            for i,k in enumerate(points):
                elem_in_dict = points.get(k)
                print(speeds[i][0], speeds[i][1])
                file.write(str(elem_in_dict[0]) + '          ' + str(elem_in_dict[1]) + '          ' + str(speeds[i][0]) + '          ' + str(speeds[i][1]) + '\n')
            
    @staticmethod
    def load_from_folder(name: str):
        name = name + '.txt'
        points_dict = {}
        list_speeds = []
        # print(os.getcwd())
        with open(name, "r") as file:
            i = 0
            for line in file.readlines():
                key = 'p' + str(i)
                print(line)
                after = 0
                before = 0
                
                line_elems = []
                while line[after] != '\n':
                    while line[after] == ' ':
                        after += 1
                    before = after
                    
                    while line[after] != ' ' and line[after] != '\n':  # Fix: added condition for newline
                        after += 1
                        
                    line_elems.append(int(float(line[before:after])))  # Fix: Convert string to int
                
                x_coord, y_coord, x_speed, y_speed = line_elems
                
                points_dict.update({key: [x_coord, y_coord, i * 100]})
                list_speeds.append([x_speed, y_speed])
                i += 1
        return points_dict, list_speeds
                