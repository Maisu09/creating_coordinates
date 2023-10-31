import cv2 as cv
import os
import tkinter as tk
from tkinter import filedialog

image = None
points_x = [40, 100]  # Your existing list of X coordinates
points_y = [50, 599]  # Your existing list of Y coordinates
dragging = None
offset_x = 0
offset_y = 0


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
    edges = cv.Canny(img, 100, 200)
    print(edges)
    # printing the result
    cv.imshow('image', img)

    cv.imshow('Edges', edges)

    cv.waitKey(0)
    cv.destroyAllWindows()


def threshold_obj_detection(img):
    """ Detecting the object with contour method and threshold """
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    threshold = 255 - threshold

    contours, hierarchy = cv.findContours(threshold, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    img_copy = img.copy()
    cv.drawContours(img_copy, contours, -1, (0, 0, 255), 2)
    cv.imshow('threshold', threshold)

    save_traced_img(img_copy)

    cv.imshow('image', img_copy)
    cv.waitKey(0)


def save_traced_img(img_copy):
    """ Takes as parameter the traced image and saves it in the out folder """

    os.chdir("..")
    # print(os.getcwd())

    try:
        os.chdir(rf'{os.getcwd()}' + '\\' + 'poze_generate')
        # print(os.getcwd())

        cv.imwrite('image.jpg', img_copy)
        # print(os.listdir())

    except os.getcwd() != r'C:\Users\mflor\Desktop\Licenta':
        print('The current working directory is not well defined!')


def load_image():
    global image
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv.imread(file_path)


def draw_points():
    if image is not None:
        for x, y in zip(points_x, points_y):
            cv.circle(image, (x, y), 5, (0, 0, 255), -1)
        update_image()


def update_image():
    if image is not None:
        cv.imshow("Image with Points", image)


def save_image_with_points():
    if image is not None:
        for x, y in zip(points_x, points_y):
            cv.circle(image, (x, y), 5, (0, 0, 255), -1)
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file_path:
            cv.imwrite(file_path, image)


def on_drag_start(event):
    global dragging, offset_x, offset_y
    if image is not None:
        x, y = event.x, event.y
        for i in range(len(points_x)):
            px, py = points_x[i], points_y[i]
            if abs(x - px) < 5 and abs(y - py) < 5:
                dragging = i
                offset_x = x - px
                offset_y = y - py


def on_drag(event):
    if dragging is not None:
        x, y = event.x, event.y
        points_x[dragging] = x - offset_x
        points_y[dragging] = y - offset_y
        update_image()


def on_drag_end(event):
    global dragging
    dragging = None


def moving_points():
    root = tk.Tk()
    root.title("Image Point Editor")

    # Create GUI elements
    load_button = tk.Button(root, text="Load Image", command=load_image)
    load_button.pack()

    draw_button = tk.Button(root, text="Draw Points", command=draw_points)
    draw_button.pack()

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()
    canvas.bind("<ButtonPress-1>", on_drag_start)
    canvas.bind("<B1-Motion>", on_drag)
    canvas.bind("<ButtonRelease-1>", on_drag_end)

    save_button = tk.Button(root, text="Save Image with Points", command=save_image_with_points)
    save_button.pack()

    # OpenCV window
    cv.namedWindow("Image with Points", cv.WINDOW_NORMAL)

    # Start the main loop
    root.mainloop()
    cv.destroyAllWindows()


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
