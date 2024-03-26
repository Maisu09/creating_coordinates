import tkinter as tk
from tkinter import filedialog
import cv2 as cv2
from ImageManipulation import ImageManipulation

# global variables
image1 = None
image2 = None
file_path1 = ''
file_path2 = ''
points1 = {
    "p0": [100, 100, 0],
    "p1": [200, 200, 100],
    "p2": [300, 300, 200],
}
points2 = points1.copy()


def clicked_at(event):
    print(f"clicked:{event.x}, {event.y}")


def points_drawing():
    global image1, file_path1, points1, image2, file_path2, points2
    if (image1 is not None) and (image2 is not None):
        ImageManipulation(points1, file_path1, image1, file_path2, image2)


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


def main():
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
    
    canvas = tk.Canvas(root, width=300, height=300)
    canvas.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
