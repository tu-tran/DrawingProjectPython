from tkinter import *

class DrawingCanvas(Frame):
    """
    Drawing canvas
    """

    def __init__(self, parent, colorPicker, cnf={}, **kw):
        Frame.__init__(self, parent)
        self.colorPicker = colorPicker
        self.isModified = False
        self.activeCommand = None
        self.startPoint = None
        self.drawObject = None

        canvas = Canvas(self, relief=SUNKEN)
        canvas.config(cnf)
        canvas.config(scrollregion=(0,0,300, 1000))
        canvas.config(highlightthickness=0)

        scrollBar = Scrollbar(self)
        scrollBar.config(command=canvas.yview)
        canvas.config(yscrollcommand=scrollBar.set)
        scrollBar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, expand=YES, fill=BOTH)
        self.canvas = canvas

    def bind(self, sequence=None, func=None, add=None):
        self.canvas.bind(sequence, func, add)

    def getShapeColor(self):
        return self.colorPicker.color

    def getDrawArea(self):
        return self.canvas