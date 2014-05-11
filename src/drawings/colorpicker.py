from tkinter import colorchooser


class ColorPicker(object):
    """
    Color picker
    """

    def __init__(self, parent):
        """
        Initializes a new instance of the color picker
        """
        self.color = "red"

    def getColor(self):
        """
        Gets the selected color.
        """
        return self.color

    def selectColor(self, parent=None):
        """
        Prompts the user to select a new color.
        """
        (rgb, hx) = colorchooser.askcolor(self.color, parent=parent)
        if hx:
            self.color = hx
        print("Selected color: " + self.color)