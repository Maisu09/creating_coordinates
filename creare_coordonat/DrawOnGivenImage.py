import cv2
import tkinter
from tkinter import filedialog


class DrawOnGivenImage:
    selected_point_index = None

    def __init__(self, points: dict, path):
        self.image = cv2.imread(path)
        self.points = points
        self.selected_points_index = None
        self.window_name = 'Move Points with Mouse'

        root = tkinter.Tk()

        cv2.namedWindow(self.window_name)
        cv2.imshow(self.window_name, self.image)
        cv2.setMouseCallback(self.window_name, self.on_mouse_event)

        add_button = tkinter.Button(root, text='Add Point', command=self.set_points_list_add)
        add_button.pack()
        save_button = tkinter.Button(root, text='Save', command=self.save_image)
        save_button.pack()

        root.mainloop()
        cv2.destroyAllWindows()

    def set_points_list_add(self):
        pass
        # self.points.append((500, 500))

    def save_image(self):
        path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if path:
            cv2.imwrite(path, self.image)

    def draw_points(self):
        image_copy = self.image.copy()

        for i, k in enumerate(self.points):
            values_of_dict = self.points.get(k)
            x = values_of_dict[0]
            y = values_of_dict[1]

            color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)
            cv2.circle(image_copy, (x, y), 10, color, -1)

        cv2.imshow(self.window_name, image_copy)

    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, k in enumerate(self.points):

                values_of_dict = self.points.get(k)
                x = values_of_dict[0]
                y = values_of_dict[1]

                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i

        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None

        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            key = "p" + str(self.selected_point_index)
            self.points.update({key: (mouse_x, mouse_y)})

        self.draw_points()
