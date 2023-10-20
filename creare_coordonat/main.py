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
    # img = cv.imread('face1.jpg', cv.IMREAD_COLOR)
    #
    # cv.imshow('image', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    #
    # print(change_dir_picture.__doc__)

    #getting the contour
    img = cv.imread('face1.jpg')
    assert img is not None, "file could not be read, check with os.path.exists()"
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(contours)

    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()




if __name__ == "__main__":
    main()
