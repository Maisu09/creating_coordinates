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
    img = cv.imread('face1.jpg', cv.IMREAD_COLOR)

    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print(change_dir_picture.__doc__)


if __name__ == "__main__":
    main()
