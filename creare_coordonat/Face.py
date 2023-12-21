class Face:
    def __init__(self, filepath='', image='', window_name=''):
        self._filepath = filepath
        self._image = image
        self._window_name = window_name

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        self._filepath = filepath

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def window_name(self):
        return self._window_name

    @window_name.setter
    def window_name(self, window_name):
        self._window_name = window_name
