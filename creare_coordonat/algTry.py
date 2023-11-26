# import cv2 as cv2
# import numpy as np
#
# # img = cv.imread('face1.jpg')
# # gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
# #
# # # cleaning img
# # ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# # print(threshold)
# # kernel = np.ones((5, 5), np.uint8)
# # opening = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)
# #
# # contours, hierarchy = cv.findContours(gray,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
# #
# # cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
# #
# # cv.imshow('image', img_copy)
# # cv.waitKey(0)
#
# # img = cv.imread('face1.jpg', cv.IMREAD_GRAYSCALE)
# # img_copy = cv.imread('face1.jpg')
# # # gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
# # # gray_invert = cv.bitwise_not(gray)
# # # edges = cv.Canny(img, 100, 200)
# #
# # # cleaning img
# # ret, threshold = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# # print(threshold)
# # kernel = np.ones((5, 5), np.uint8)
# # opening = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
# #
# # # # img_copy = cv.imread("face1 (1).jpg.jpg")
# #
# # contours, hierarchy = cv.findContours(img,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
# # # print("Numar de conture: {}\n".format(len(contours)))
# #
# # cv.drawContours(img, contours, -1, (0, 255, 0), 3)
# #
# # cv.imshow('image', img + threshold)
# # cv.waitKey(0)
# #
# #
#
#
# # # Generare puncte prin contours.
# # img = cv2.imread('unu.jpg')
# # # gray = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
# #
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# # threshold = 255 - threshold
# #
# # contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# #
# # cv2.imwrite('box_contour.jpg', img)
# #
# # img_copy = img.copy()
# # cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
# #
# # cv2.imshow('threshold', threshold)
# # cv2.imshow('image', img_copy)
# # cv2.waitKey(0)
#
# # def GUI1():
# #     # GUI
# #
# #     import PySimpleGUI as sg
# #     import os.path
# #
# #     # First the window layout in 2 columns
# #
# #     file_list_column = [
# #         [
# #             sg.Text("Image Folder"),
# #             sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
# #             sg.FolderBrowse(),
# #         ],
# #         [
# #             sg.Listbox(
# #                 values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
# #             )
# #         ],
# #     ]
# #
# #     # For now will only show the name of the file that was chosen
# #     image_viewer_column = [
# #         [sg.Text("Choose an image from list on left:")],
# #         [sg.Text(size=(40, 1), key="-TOUT-")],
# #         [sg.Image(key="-IMAGE-")],
# #     ]
# #
# #     # ----- Full layout -----
# #     layout = [
# #         [
# #             sg.Column(file_list_column),
# #             sg.VSeperator(),
# #             sg.Column(image_viewer_column),
# #         ]
# #     ]
# #
# #     window = sg.Window("Image Viewer", layout)
# #
# #     # Run the Event Loop
# #     while True:
# #         event, values = window.read()
# #         if event == "Exit" or event == sg.WIN_CLOSED:
# #             break
# #         # Folder name was filled in, make a list of files in the folder
# #         if event == "-FOLDER-":
# #             folder = values["-FOLDER-"]
# #             try:
# #                 # Get list of files in folder
# #                 file_list = os.listdir(folder)
# #             except:
# #                 file_list = []
# #
# #             fnames = [
# #                 f
# #                 for f in file_list
# #                 if os.path.isfile(os.path.join(folder, f))
# #                 and f.lower().endswith((".png", ".jpg"))
# #             ]
# #             window["-FILE LIST-"].update(fnames)
# #         elif event == "-FILE LIST-":  # A file was chosen from the listbox
# #             try:
# #                 filename = os.path.join(
# #                     values["-FOLDER-"], values["-FILE LIST-"][0]
# #                 )
# #                 window["-TOUT-"].update(filename)
# #                 window["-IMAGE-"].update(filename=filename)
# #
# #             except:
# #                 pass
# #
# #     window.close()
#
# # import sys
# # import cv2
# # import numpy as np
# # from PyQt5.QtCore import Qt, QPoint
# # from PyQt5.QtGui import QImage, QPixmap
# # from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# # class ImagePointMover(QMainWindow):
# #     def __init__(self, image_path):
# #         super().__init__()
# #         self.image = cv2.imread(image_path)
# #         self.image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
# #         self.height, self.width, _ = self.image.shape
# #         self.setWindowTitle("Image Point Mover")
# #         self.setGeometry(100, 100, self.width, self.height)
# #
# #         self.image_label = QLabel()
# #         self.image_label.setAlignment(Qt.AlignCenter)
# #         self.image_label.setMouseTracking(True)
# #
# #         self.central_widget = QWidget()
# #         self.setCentralWidget(self.central_widget)
# #         layout = QVBoxLayout(self.central_widget)
# #         layout.addWidget(self.image_label)
# #
# #         self.points = []  # List to store points (x, y)
# #
# #         self.load_image()
# #         self.image_label.mouseMoveEvent = self.mouse_move
# #
# #     def load_image(self):
# #         q_image = QImage(
# #             self.image_rgb.data, self.width, self.height, self.width * 3, QImage.Format_RGB888
# #         )
# #         pixmap = QPixmap.fromImage(q_image)
# #         self.image_label.setPixmap(pixmap)
# #
# #     def mouse_move(self, event):
# #         if event.buttons() == Qt.LeftButton:
# #             x, y = event.x(), event.y()
# #             self.points.append((x, y))
# #             cv2.circle(self.image, (x, y), 3, (0, 0, 255), -1)
# #             self.load_image()
# #
# # if __name__ == '__main__':
# #     if len(sys.argv) != 2:
# #         print("Usage: python image_point_mover.py <image_path>")
# #         sys.exit(1)
# #
# #     app = QApplication(sys.argv)
# #     image_path = sys.argv[1]
# #     window = ImagePointMover(image_path)
# #     window.show()
# #     sys.exit(app.exec_())
#
# # import pygame
# #
# # pygame.init()
# #
# # size = [400, 500]
# # screen = pygame.display.set_mode(size)
# #
# # done = False
# #
# # while done == False:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             done = True
# #
# #     screen.fill()
#
# #
# # import cv2
# # import tkinter as tk
# # from tkinter import filedialog
# # import numpy as np
# #
# # # Define global variables to store the image and points
# # image = None
# # points = []
# #
# # def load_image():
# #     global image, points
# #     file_path = filedialog.askopenfilename()
# #     if file_path:
# #         image = cv2.imread(file_path)
# #         points = []
# #
# # def draw_points(event):
# #     if image is not None:
# #         x, y = event.x, event.y
# #         points.append((x, y))
# #         cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
# #         update_image()
# #
# # def update_image():
# #     if image is not None:
# #         cv2.imshow("Image with Points", image)
# #
# # def save_image_with_points():
# #     if image is not None:
# #         for point in points:
# #             cv2.circle(image, point, 5, (0, 0, 255), -1)
# #         file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
# #         if file_path:
# #             cv2.imwrite(file_path, image)
# #
# # # Create the main window
# # root = tk.Tk()
# # root.title("Image Point Editor")
# #
# # # Create GUI elements
# # load_button = tk.Button(root, text="Load Image", command=load_image)
# # load_button.pack()
# #
# # canvas = tk.Canvas(root, width=800, height=600)
# # canvas.pack()
# # canvas.bind("<Button-1>", draw_points)
# #
# # save_button = tk.Button(root, text="Save Image with Points", command=save_image_with_points)
# # save_button.pack()
# #
# # # OpenCV window
# # cv2.namedWindow("Image with Points", cv2.WINDOW_NORMAL)
# #
# # # Start the main loop
# # root.mainloop()
# # cv2.destroyAllWindows()
# # #
# # import cv2
# # import tkinter as tk
# # from tkinter import filedialog
# # import numpy as np
# #
# # # Define global variables to store the image and points
# # image = None
# # points_x = []
# # points_y = []
# # dragging = None
# # offset_x = 0
# # offset_y = 0
# #
# # def load_image():
# #     global image, points_x, points_y
# #     file_path = filedialog.askopenfilename()
# #     if file_path:
# #         image = cv2.imread(file_path)
# #         points_x = []
# #         points_y = []
# #
# # def draw_points(event):
# #     if image is not None:
# #         x, y = event.x, event.y
# #         points_x.append(x)
# #         points_y.append(y)
# #         cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
# #         update_image()
# #
# # def update_image():
# #     if image is not None:
# #         for i in range(len(points_x)):
# #             x, y = points_x[i], points_y[i]
# #             cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
# #         cv2.imshow("Image with Points", image)
# #
# # def save_image_with_points():
# #     if image is not None:
# #         for i in range(len(points_x)):
# #             x, y = points_x[i], points_y[i]
# #             cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
# #         file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
# #         if file_path:
# #             cv2.imwrite(file_path, image)
# #
# # def on_drag_start(event):
# #     global dragging, offset_x, offset_y
# #     if image is not None:
# #         x, y = event.x, event.y
# #         for i in range(len(points_x)):
# #             px, py = points_x[i], points_y[i]
# #             if abs(x - px) < 5 and abs(y - py) < 5:
# #                 dragging = i
# #                 offset_x = x - px
# #                 offset_y = y - py
# #
# # def on_drag(event):
# #     if dragging is not None:
# #         x, y = event.x, event.y
# #         points_x[dragging] = x - offset_x
# #         points_y[dragging] = y - offset_y
# #         update_image()
# #
# # def on_drag_end(event):
# #     global dragging
# #     dragging = None
# #
# # # Create the main window
# # root = tk.Tk()
# # root.title("Image Point Editor")
# #
# # # Create GUI elements
# # load_button = tk.Button(root, text="Load Image", command=load_image)
# # load_button.pack()
# #
# # canvas = tk.Canvas(root, width=800, height=600)
# # canvas.pack()
# # canvas.bind("<Button-1>", draw_points)
# # canvas.bind("<ButtonPress-1>", on_drag_start)
# # canvas.bind("<B1-Motion>", on_drag)
# # canvas.bind("<ButtonRelease-1>", on_drag_end)
# #
# # save_button = tk.Button(root, text="Save Image with Points", command=save_image_with_points)
# # save_button.pack()
# #
# # # OpenCV window
# # cv2.namedWindow("Image with Points", cv2.WINDOW_NORMAL)
# #
# # # Start the main loop
# # root.mainloop()
# # cv2.destroyAllWindows()
#
# import cv2
# import tkinter as tk
# from tkinter import filedialog
# import numpy as np
#
# # Define global variables to store the image and points
# image = None
# points_x = [40, 100]  # Your existing list of X coordinates
# points_y = [50, 599]  # Your existing list of Y coordinates
# selected_point = None
# offset_x = 0
# offset_y = 0
#
#
# def load_image():
#     global image
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         image = cv2.imread(file_path)
#
#
# def draw_points():
#     if image is not None:
#         for x, y in zip(points_x, points_y):
#             cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
#         update_image()
#
#
# def update_image():
#     if image is not None:
#         cv2.imshow("Image with Points", image)
#
#
# def save_image_with_points():
#     if image is not None:
#         for x, y in zip(points_x, points_y):
#             cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
#         file_path = filedialog.asksaveasfilename(defaultextension=".jpg")
#         if file_path:
#             cv2.imwrite(file_path, image)
#
#
# def on_drag_start(event):
#
#     global selected_point, offset_x, offset_y
#     if image is not None:
#         x, y = event.x, event.y
#         for i in range(len(points_x)):
#             px, py = points_x[i], points_y[i]
#             if abs(x - px) < 5 and abs(y - py) < 5:
#                 selected_point = i
#                 offset_x = x - px
#                 offset_y = y - py
#                 break
#
#
# def on_drag(event):
#     if selected_point is not None:
#         x, y = event.x, event.y
#         points_x[selected_point] = x - offset_x
#         points_y[selected_point] = y - offset_y
#         update_image()
#
#
# def on_drag_end(event):
#     global selected_point
#     selected_point = None
#
#
# # Create the main window
# root = tk.Tk()
# root.title("Image Point Editor")
#
# # Create GUI elements
# load_button = tk.Button(root, text="Load Image", command=load_image)
# load_button.pack()
#
# draw_button = tk.Button(root, text="Draw Points", command=draw_points)
# draw_button.pack()
#
# canvas = tk.Canvas(root, width=800, height=600)
# canvas.pack()
# canvas.bind("<Button-1>", on_drag_start)
# canvas.bind("<B1-Motion>", on_drag)
# canvas.bind("<ButtonRelease-1>", on_drag_end)
#
# save_button = tk.Button(root, text="Save Image with Points", command=save_image_with_points)
# save_button.pack()
#
# # OpenCV window
# cv2.namedWindow("Image with Points", cv2.WINDOW_NORMAL)
#
# # Start the main loop
# root.mainloop()
# cv2.destroyAllWindows()


# import cv2
#
# # Load an image as the canvas
# image = cv2.imread('C:\\Users\\mflor\\Desktop\\Licenta\\poze_initiale\\face1.jpg')  # Replace 'your_image.jpg' with the path to your image
# if image is None:
#     print("Error: Could not load the image.")
#     exit()
#
# # Ensure that the canvas is in the correct format (BGR)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# # Initial list of points
# points = [(200, 200), (300, 300), (100, 100)]
# selected_point_index = None
#
# def draw_points():
#     image_copy = image.copy()
#     for i, (x, y) in enumerate(points):
#         color = (255, 0, 0) if i == selected_point_index else (0, 255, 0)
#         cv2.circle(image_copy, (x, y), 10, color, -1)
#     cv2.imshow(window_name, image_copy)
#
# window_name = 'Move Points with Mouse'
# cv2.namedWindow(window_name)
# cv2.imshow(window_name, image)
#
# def on_mouse_event(event, mouse_x, mouse_y, flags, param):
#     global selected_point_index
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         for i, (x, y) in enumerate(points):
#             if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
#                 selected_point_index = i
#     elif event == cv2.EVENT_LBUTTONUP:
#         selected_point_index = None
#     elif event == cv2.EVENT_MOUSEMOVE and selected_point_index is not None:
#         points[selected_point_index] = (mouse_x, mouse_y)
#     draw_points()
#
# cv2.setMouseCallback(window_name, on_mouse_event)
#
# while True:
#     key = cv2.waitKey(30)
#     if key == ord('q'):
#         break
#
# cv2.destroyAllWindows()
#
# import cv2
# import DrawOnGivenImage

# aa = DrawOnGivenImage.DrawOnGivenImage([(200, 200), (300, 300), (100, 100)] ,'C:\\Users\\mflor\\Desktop\\Licenta\\poze_initiale\\face1.jpg')


# points = {
#     "p0": [200, 200],
#     "p1": [300, 300],
#     "p2": [100, 100],
# }
# letter = "p"
# i = 0
# points.update({"p0": [100, 200]})
#
#
# print(points.get(letter + str(i)))
#
#

# for i, k in enumerate(points):
#     # print(i)
#     print(k)
#     print(points.get(k))
#     element_values = points.get(k)
#     x = element_values[0]
#     y = element_values[1]
#     print(x, y)

import numpy as np
import cv2

# Define the coefficients of the third-degree equation (ax^3 + bx^2 + cx + d)
a, b, c, d = 1, -6, 11, -6  # Replace these with your coefficients

# Define the starting and ending points for the plot
start_point = -2
end_point = 4

# Generate x values between the starting and ending points
x_values = np.linspace(start_point, end_point, 1000)

# Calculate corresponding y values using the third-degree equation
y_values = a * x_values**3 + b * x_values**2 + c * x_values + d

# Normalize the y values to fit within the image height
y_values_normalized = (y_values - np.min(y_values)) / (np.max(y_values) - np.min(y_values))

# Create an image to plot the equation
img_height = 400
img_width = 600
img = np.ones((img_height, img_width, 3), dtype=np.uint8) * 255  # White background

# Scale and shift x values to fit within the image width
x_values_scaled = ((x_values - start_point) / (end_point - start_point)) * (img_width - 1)

# Scale and shift y values to fit within the image height
y_values_scaled = ((1 - y_values_normalized) * (img_height - 1)).astype(int)

# Plot the points on the image
for x, y in zip(x_values_scaled, y_values_scaled):
    cv2.circle(img, (int(x), int(y)), 2, (0, 0, 0), -1)  # Draw a black circle

# Show the image with the plotted equation
cv2.imshow('Equation Plot', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



