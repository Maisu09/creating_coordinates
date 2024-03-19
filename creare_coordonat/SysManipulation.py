import os
import cv2


class SysManipulation:

    @staticmethod
    def create_folder_in_dir(folder_name:str):
        """ Changing wd to the directory where images are stored. """
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print('folder exist')
            
        os.chdir(folder_name)
        print(os.getcwd())
        
        
    @staticmethod
    def save_points(points:dict, name:str):
        """  """
        ## primeste puncte schimba directoru in ala creat face dupa un fisier in care salveaza cu open punctele din image man.
        name.strip()
        name = name +'.txt'
        with open(name, 'w') as file:
            # file.write('x          y \n')
            
            for i,k in enumerate(points):
                elem_in_dict = points.get(k)
                file.write(str(elem_in_dict[0]) + '          ' + str(elem_in_dict[1])+'\n')

    @staticmethod
    def load_from_folder(name:str):
        name = name + '.txt'
        points_dict={}
        # print(os.getcwd())
        with open(name, "r") as file:
            i = 0
            for line in file.readlines():
                key = 'p' + str(i)
                print(line)
                j=0
                while line[j] is not ' ':
                    j += 1
                
                x_coord = int(line[:j])
                print(x_coord)
                line = line[j:]
                line.strip()
                y_coord = int(line)
                print(y_coord)
                
                points_dict.update({key: [x_coord, y_coord, i*100]})
                i += 1
        return points_dict
                
                
            
                
             