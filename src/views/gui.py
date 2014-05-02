from tkinter import Image, PhotoImage, Frame, Button, LEFT, TOP, X, FLAT, RAISED, YES, BOTH, GROOVE, RIDGE, SUNKEN, RAISED
from views.resourcemanager import ResourceManager, DefaultResourceManager
from drawings.canvas import DrawingCanvas
from drawings.colorpicker import ColorPicker
from functools import partial


class GUI(object):
    """
    The base class for GUI builder
    """

    def __init__(self, root):
        self.colorPicker = ColorPicker(root)
        self.topToolbar = Frame(root, bd=1, relief=RAISED)
        self.topToolbar.pack(side=TOP, fill=X)
        self.canvas = DrawingCanvas(root, self.colorPicker)
        self.canvas.pack(expand=YES, fill=BOTH)

    def initButtons(self, ios, commands):
        pass

    def onIOCommandClick(self, button, command):
        pass

    def onDrawCommandClick(self, button, command):
        pass

    def onChangeColor(self, command):
        pass


class ClassicGUI(GUI):
    """
    The classical GUI builder
    """

    def __init__(self, root):
        GUI.__init__(self, root)
        self.root = root
        self.res = DefaultResourceManager()     # The default resource manager providing tool bar icons

    def initButtons(self, ios, commands):
        for command in ios:
            cmdInstance = command()
            cmdButton = Button(self.topToolbar, image=self.res.get(command.getId()), relief=GROOVE)
            cmdHandler = partial(self.onIOCommandClick, cmdButton, cmdInstance)
            cmdButton.config(command=cmdHandler)
            cmdButton.pack(side=LEFT, padx=2, pady=2)

        self.commandButtons = []
        for command in commands:
            cmdButton = Button(self.topToolbar, image=self.res.get(command.getId()), relief=FLAT)
            cmdHandler = partial(self.onDrawCommandButtonClick, cmdButton, command)
            cmdButton.config(command=cmdHandler)
            cmdButton.pack(side=LEFT, padx=2, pady=2)
            self.commandButtons.append(cmdButton)

        cmdColorPicker = Button(self.topToolbar, relief=RIDGE)
        cmdHandler = partial(self.onChangeColor, cmdColorPicker)
        cmdColorPicker.config(command=cmdHandler, background=self.colorPicker.getColor(), relief=GROOVE, width=2, highlightbackground='white')
        cmdColorPicker.pack(side=LEFT, padx=15, pady=2)

    def onChangeColor(self, button):
        self.colorPicker.selectColor(self.root)
        button.config(background=self.colorPicker.getColor())
        
    def onDrawCommandButtonClick(self, button, command):
        # Reset relief state of other buttons
        for btn in self.commandButtons:
            if btn is not button:
                btn.config(relief=FLAT)
                
        # Set relief state for active command button
        button.config(relief=SUNKEN)
        self.onDrawCommandClick(button, command)
