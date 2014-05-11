from tkinter import *


class DrawingCanvas(Frame):
    """
    Drawing canvas
    """

    DEFAULT_WIDTH = 500
    DEFAULT_HEIGHT = 500

    def __init__(self, parent, colorPicker):
        """
        Initiliazes a new instance of the drawing canvas. It takes the Tkinter root and the color picker as parameters.
        """
        Frame.__init__(self, parent)
        self.config(bg='grey')
        self.colorPicker = colorPicker
        self.isModified = False
        self.activeCommand = None
        self.startPoint = None
        self.drawObject = None

        canvas = Canvas(self, relief=SUNKEN, width=self.DEFAULT_WIDTH, height=self.DEFAULT_HEIGHT, bg='white',
                        highlightthickness=0)
        vScrollBar = Scrollbar(self, orient=VERTICAL, command=canvas.yview)
        vScrollBar.pack(side=RIGHT, fill=Y)
        hScrollBar = Scrollbar(self, orient=HORIZONTAL, command=canvas.xview)
        hScrollBar.pack(side=BOTTOM, fill=X)
        canvas.config(scrollregion=(0, 0, self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT))
        canvas.config(xscrollcommand=hScrollBar.set, yscrollcommand=vScrollBar.set)

        canvas.pack(side=LEFT, expand=YES)
        self.canvas = canvas

    def bind(self, sequence=None, func=None, add=None):
        """
        Wrapper method for binding certain events to the underneath Tkinter drawing canvas.
        """
        self.canvas.bind(sequence, func, add)

    def getShapeColor(self):
        """
        Get the selected shape color
        """
        return self.colorPicker.color

    def getDrawArea(self):
        """
        Get the actual Tkinter drawing canvas object.
        """
        return self.canvas