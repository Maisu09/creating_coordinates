import cv2 as cv
import os


def change_dir_picture():
    '''Changing wd to the directory where images are stored.'''
    pass
    # if os.getcwd() == r'../crerare_coordonate':
    #     os.chdir(r'/Licenta/poze')
    #
    # print((os.getcwd()))
    #


def main():
    # change_dir_picture()
    # reading image
    img = cv.imread('face1.jpg', 0)
    assert img is not None, "file could not be read, check with os.path.exists()"

    img_copy = cv.imread('face1.jpg')
    assert img_copy is not None, "file could not be read, check with os.path.exists()"

    # gray scaling the image and reversing it.
    gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
    gray_invert = cv.bitwise_not(gray)

    # generating the contours
    contours = cv.findContours(gray_invert, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # print(contours)

    # creating the edges (method 2)
    edges = cv.Canny(img, 100, 200)
    print(edges)
    # printing the result
    cv.imshow('image', img)

    cv.imshow('Edges', edges)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
