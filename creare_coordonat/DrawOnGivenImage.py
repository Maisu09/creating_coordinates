import cv2


class DrawOnGivenImage:
    selected_point_index = None

    def __init__(self, points: list, path):
        self.image = cv2.imread(path)
        self.points = points
        self.selected_points_index = None
        self.window_name = 'Move Points with Mouse'
        cv2.namedWindow(self.window_name)
        cv2.imshow(self.window_name, self.image)
        cv2.setMouseCallback(self.window_name, self.on_mouse_event)

        while True:
            key = cv2.waitKey(30)
            if key == ord('q'):
                break

        cv2.destroyAllWindows()

    def draw_points(self):
        image_copy = self.image.copy()
        for i, (x, y) in enumerate(self.points):
            color = (255, 0, 0) if i == self.selected_point_index else (0, 255, 0)
            cv2.circle(image_copy, (x, y), 10, color, -1)
        cv2.imshow(self.window_name, image_copy)

    def on_mouse_event(self, event, mouse_x, mouse_y, flags, param, selected_point_index=None):
        if event == cv2.EVENT_LBUTTONDOWN:
            for i, (x, y) in enumerate(self.points):
                if abs(x - mouse_x) < 10 and abs(y - mouse_y) < 10:
                    self.selected_point_index = i
        elif event == cv2.EVENT_LBUTTONUP:
            self.selected_point_index = None
        elif event == cv2.EVENT_MOUSEMOVE and self.selected_point_index is not None:
            self.points[self.selected_point_index] = (mouse_x, mouse_y)

        self.draw_points()
