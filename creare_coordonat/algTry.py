import cv2 as cv2
import numpy as np

# img = cv.imread('face1.jpg')
# gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
#
# # cleaning img
# ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(threshold)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)
#
# contours, hierarchy = cv.findContours(gray,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
#
# cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
#
# cv.imshow('image', img_copy)
# cv.waitKey(0)

# img = cv.imread('face1.jpg', cv.IMREAD_GRAYSCALE)
# img_copy = cv.imread('face1.jpg')
# # gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
# # gray_invert = cv.bitwise_not(gray)
# # edges = cv.Canny(img, 100, 200)
#
# # cleaning img
# ret, threshold = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(threshold)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#
# # # img_copy = cv.imread("face1 (1).jpg.jpg")
#
# contours, hierarchy = cv.findContours(img,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
# # print("Numar de conture: {}\n".format(len(contours)))
#
# cv.drawContours(img, contours, -1, (0, 255, 0), 3)
#
# cv.imshow('image', img + threshold)
# cv.waitKey(0)
#
#


# # Generare puncte prin contours.
# img = cv2.imread('unu.jpg')
# # gray = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
#
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# ret, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# threshold = 255 - threshold
#
# contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
# cv2.imwrite('box_contour.jpg', img)
#
# img_copy = img.copy()
# cv2.drawContours(img_copy, contours, -1, (0, 255, 0), 3)
#
# cv2.imshow('threshold', threshold)
# cv2.imshow('image', img_copy)
# cv2.waitKey(0)

def GUI1():
    # GUI

    import PySimpleGUI as sg
    import os.path

    # First the window layout in 2 columns

    file_list_column = [
        [
            sg.Text("Image Folder"),
            sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
            sg.FolderBrowse(),
        ],
        [
            sg.Listbox(
                values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
            )
        ],
    ]

    # For now will only show the name of the file that was chosen
    image_viewer_column = [
        [sg.Text("Choose an image from list on left:")],
        [sg.Text(size=(40, 1), key="-TOUT-")],
        [sg.Image(key="-IMAGE-")],
    ]

    # ----- Full layout -----
    layout = [
        [
            sg.Column(file_list_column),
            sg.VSeperator(),
            sg.Column(image_viewer_column),
        ]
    ]

    window = sg.Window("Image Viewer", layout)

    # Run the Event Loop
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        # Folder name was filled in, make a list of files in the folder
        if event == "-FOLDER-":
            folder = values["-FOLDER-"]
            try:
                # Get list of files in folder
                file_list = os.listdir(folder)
            except:
                file_list = []

            fnames = [
                f
                for f in file_list
                if os.path.isfile(os.path.join(folder, f))
                and f.lower().endswith((".png", ".jpg"))
            ]
            window["-FILE LIST-"].update(fnames)
        elif event == "-FILE LIST-":  # A file was chosen from the listbox
            try:
                filename = os.path.join(
                    values["-FOLDER-"], values["-FILE LIST-"][0]
                )
                window["-TOUT-"].update(filename)
                window["-IMAGE-"].update(filename=filename)

            except:
                pass

    window.close()