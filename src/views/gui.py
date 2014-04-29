from tkinter import Image, PhotoImage, Frame, Button, LEFT, TOP, X, FLAT, RAISED, YES, BOTH, GROOVE, RIDGE, SUNKEN
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
        self.canvas = DrawingCanvas(root, self.colorPicker, width=500, height=500, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)

    def initButtons(self, ios, commands):
        pass

    def onIOCommandClick(self, command):
        pass

    def onDrawCommandClick(self, command):
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
            cmdButton = Button(self.topToolbar, image=self.res.get(command.getId()), relief=GROOVE, command=partial(self.onIOCommandClick, command))
            cmdButton.pack(side=LEFT, padx=2, pady=2)

        self.commandButtons = []
        for command in commands:
            cmdButton = Button(self.topToolbar, image=self.res.get(command.getId()), relief=FLAT, command=partial(self.onDrawCommandButtonClick, command))
            cmdButton.pack(side=LEFT, padx=2, pady=2)
            self.commandButtons.append(cmdButton)

        cmdColorPicker = Button(self.topToolbar, relief=RIDGE)
        cmdHandler = partial(self.onChangeColor, cmdColorPicker)
        cmdColorPicker.config(command=cmdHandler)
        cmdColorPicker.config(background=self.colorPicker.getColor())
        cmdColorPicker.pack(side=LEFT, padx=5, pady=2, expand=5)

    def onChangeColor(self, button):
        self.colorPicker.selectColor(self.root)
        button.config(background=self.colorPicker.getColor())
        
    def onDrawCommandButtonClick(self, command):
        # Reset relief state of other buttons
        for btn in self.commandButtons:
            if btn is not command:
                btn.config(relief=FLAT)
                
        # Set relief state for active command button
        command.config(relief=SUNKEN)
        self.onDrawCommandClick(command)
