import cv2 as cv2
import os
import tkinter as tk
from tkinter import filedialog
from DrawOnGivenImage import DrawOnGivenImage

# global variables
image = None
is_for_moving_point = False
file_path = ''
points = {
    "p0": [200, 200, 0],
    "p1": [300, 300, 100],
    "p2": [100, 100, 200],
}


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
    global image, file_path, points
    if image is not None:
        aa = DrawOnGivenImage(points, file_path)


def load_image():
    """Loading the image from computer"""
    global image, file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)


def moving_points():
    root = tk.Tk()
    root.title("Image editor")

    # GUI elements
    load_button = tk.Button(root, text="Load image", command=load_image)
    load_button.pack()

    draw_button = tk.Button(root, text="Draw", command=points_drawing)
    draw_button.pack()

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    root.mainloop()


def main():
    moving_points()


if __name__ == "__main__":
    main()
