from tkinter import colorchooser


class ColorPicker(object):
    """
    Color picker
    """

    def __init__(self, parent):
        self.color = "red"

    def getColor(self):
        return self.color

    def selectColor(self, parent=None):
        (rgb, hx) = colorchooser.askcolor(self.color, parent=parent)
        if hx:
            self.color = hx