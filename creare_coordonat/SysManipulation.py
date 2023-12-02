import os
import cv2


class SysManipulation:

    @staticmethod
    def change_dir_picture():
        """ Changing wd to the directory where images are stored. """
        os.chdir('..')
        os.chdir(rf'{os.getcwd()}' + '\\' + 'poze_initiale')

    @staticmethod
    def save_traced_img(img_copy, has_polynom: bool):
        """ Takes as parameter the traced image and saves it in the out folder """

        os.chdir("..")
        # print(os.getcwd())

        try:
            os.chdir(rf'{os.getcwd()}' + '\\' + 'poze_generate')
            # print(os.getcwd())
            if has_polynom:
                cv2.imwrite('image1.jpg', img_copy)
            else:
                cv2.imwrite('image.jpg', img_copy)
            # print(os.listdir())
        except os.getcwd() != r'C:\Users\mflor\Desktop\Licenta':
            print('The current working directory is not well defined!')
