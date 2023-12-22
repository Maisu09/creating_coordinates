import os
import tkinter as tk
from tkinter import filedialog

import cv2 as cv2

from Face import Face
from ImageManipulation import ImageManipulation
from Image_manipulation import Image_manipulation

# global variables
image1 = None
image2 = None
is_for_moving_point = False
file_path1 = ''
file_path2 = ''
points1 = {
    "p0": [200, 200, 0],
    "p1": [300, 300, 100],
    "p2": [100, 100, 200],
}
points2 = points1


def save_traced_img(img_copy):
    """ Takes as parameter the traced image and saves it in the out folder """

    os.chdir("..")
    # print(os.getcwd())

    try:
        os.chdir(rf'{os.getcwd()}' + '\\' + 'poze_generate')
        # print(os.getcwd())

        cv2.imwrite('image.jpg', img_copy)
        # print(os.listdir())
    except os.getcwd() != r'C:\Users\mflor\Desktop\Licenta':
        print('The current working directory is not well defined!')


def clicked_at(event):
    print(f"clicked:{event.x}, {event.y}")


def points_drawing():
    global image1, file_path1, points1, image2, file_path2, points2
    if image1 is not None:
        # image_manipulation = ImageManipulation(points, file_path1, image1, file_path2, image2)
        image_man = Image_manipulation(points1, file_path1, image1, file_path2, image2, points2)


def load_image1():
    """Loading the image from computer"""
    global image1, file_path1

    file_path1 = filedialog.askopenfilename()
    if file_path1:
        image1 = cv2.imread(file_path1)


def load_image2():
    """Loading the image from computer"""
    global image2, file_path2

    file_path2 = filedialog.askopenfilename()
    if file_path2:
        image2 = cv2.imread(file_path2)


def moving_points():
    global file_path2, file_path1, image1, image2
    root = tk.Tk()
    root.title("Image editor")

    # GUI elements
    load_button1 = tk.Button(root, text="Load image1", command=load_image1)
    load_button1.pack()

    load_button2 = tk.Button(root, text="Load image2", command=load_image2)
    load_button2.pack()

    draw_button = tk.Button(root, text="Draw", command=points_drawing)
    draw_button.pack()
    print(file_path1)

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    root.mainloop()


def main():
    moving_points()


if __name__ == "__main__":
    main()
