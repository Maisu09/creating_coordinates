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
    "p0": [200, 200],
    "p1": [300, 300],
    "p2": [100, 100],
}


def change_dir_picture():
    """ Changing wd to the directory where images are stored. """
    os.chdir('..')
    # print(os.listdir())

    os.chdir(rf'{os.getcwd()}' + '\\' + 'poze_initiale')
    # print(os.getcwd())
    # print(os.listdir())


def canny_edge_detection(img):
    """ Using the canny method to determine the lines of the object """
    # creating the edges (method 2)
    edges = cv2.Canny(img, 100, 200)
    print(edges)
    # printing the result
    cv2.imshow('image', img)

    cv2.imshow('Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def threshold_obj_detection(img):
    """ Detecting the object with contour method and threshold """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    threshold = 255 - threshold

    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    img_copy = img.copy()
    cv2.drawContours(img_copy, contours, -1, (0, 0, 255), 2)
    cv2.imshow('threshold', threshold)

    save_traced_img(img_copy)

    cv2.imshow('image', img_copy)
    cv2.waitKey(0)


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
