from drawings.colorpicker import ColorPicker


class DummyColorPicker(ColorPicker):
    """
    Dummy Color Picker class used for unit testing
    """

    def selectColor(self, parent=None):
        return 'red'


class Mock(object):
    """
    Helper object used for mocking objects
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)