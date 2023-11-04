import cv2 as cv2
import os
import tkinter as tk
from tkinter import filedialog

image = None
points_x = [200]  # Your existing list of X coordinates
points_y = [200]  # Your existing list of Y coordinates
dragging = None
draw = False
ix, iy = -1, -1
is_for_moving_point = False
close_to_point = [3, 3]



def change_dir_picture():
    """ Changing wd to the directory where images are stored. """
    # print(os.getcwd())

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

def moved_the_point(x, y):
    cv2.

def get_coord(event, x, y, flags, param):
    """Verify if the mouse is clicked and prints the position. Also prints the position for the moving mouse."""
    global draw, ix, iy, is_for_moving_point

    if event == cv2.EVENT_LBUTTONDOWN:
        if (
                (x + close_to_point[0] == points_x[0] or x - close_to_point[0] == points_x[0]) and
                (y + close_to_point[0] == points_y[0] or y - close_to_point[0] == points_y[0])
        ):
            is_for_moving_point = True
        print(f"clicked:{x}, {y}")
        draw = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == True:
            print(f"Clicked:{ix}, {iy}; {x}, {y}")

    elif event == cv2.EVENT_LBUTTONUP:
        draw = False
        print(f"Last position: {x}, {y}")
        if is_for_moving_point:
            moved_the_point(x, y)
        is_for_moving_point = False


def clicked_at(event):
    print(f"clicked:{event.x}, {event.y}")


def draw_points():
    global image
    if image is not None:
        image = cv2.circle(image, (points_x[0], points_y[0]), 1, (0, 0, 255), 2)
        cv2.imshow("Image", image)

    cv2.setMouseCallback("Image", get_coord)


def load_image():
    """Loading the image from computer"""
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)


def moving_points():
    root = tk.Tk()
    root.title("Image editor")

    # GUI elements
    load_button = tk.Button(root, text="Load image", command=load_image)
    load_button.pack()

    draw_button = tk.Button(root, text="Draw", command=draw_points)
    draw_button.pack()

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    #Click position in the upload image area not on img
    # canvas.bind("<Button-1>", clicked_at)

    root.mainloop()


def main():
    # change_dir_picture()

    # reading image
    # img = cv.imread('unu.jpg')
    # assert img is not None, "file could not be read, check with os.path.exists()"

    # object detection and contour draw
    # threshold_obj_detection(img)
    moving_points()


if __name__ == "__main__":
    main()
