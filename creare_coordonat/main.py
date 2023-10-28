import cv2 as cv
import os


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


def main():
    change_dir_picture()

    # reading image
    img = cv.imread('unu.jpg')
    assert img is not None, "file could not be read, check with os.path.exists()"

    # object detection and contour draw
    threshold_obj_detection(img)


if __name__ == "__main__":
    main()
