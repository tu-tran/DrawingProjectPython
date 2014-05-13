from abc import ABCMeta, abstractmethod
from tkinter import Frame, Button, LEFT, TOP, X, FLAT, YES, BOTH, GROOVE, RIDGE, SUNKEN, RAISED
from functools import partial

from src.views.resourcemanager import DefaultResourceManager
from src.drawings.canvas import DrawingCanvas
from src.drawings.colorpicker import ColorPicker


class GUI(object):
    """
    The base class for GUI builder
    """

    __metaclass__ = ABCMeta

    def __init__(self, root):
        self.colorPicker = ColorPicker(root)
        self.topToolbar = Frame(root, bd=1, relief=RAISED)
        self.topToolbar.pack(side=TOP, fill=X)
        self.canvas = DrawingCanvas(root, self.colorPicker)
        self.canvas.pack(expand=YES, fill=BOTH)

    # Initializes IO and Draw commands.
    @abstractmethod
    def initButtons(self, ios, commands):
        pass

    # Event handler when users click on an IO command.
    @abstractmethod
    def onIOCommandClick(self, button, command):
        pass

    # Event handler when users click on a draw command.
    @abstractmethod
    def onDrawCommandClick(self, button, command):
        pass

    # Event handler when users change the selected color.
    @abstractmethod
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
        self.ioButtons = []
        self.commandButtons = []

    # Initializes IO and Draw commands.
    def initButtons(self, ios, commands):
        for command in ios:
            cmdInstance = command()
            cmdButton = Button(self.topToolbar, image=self.res.get(command.get_id()), relief=GROOVE)
            cmdHandler = partial(self.onIOCommandClick, cmdButton, cmdInstance)
            cmdButton.config(command=cmdHandler)
            cmdButton.pack(side=LEFT, padx=2, pady=2)
            self.ioButtons.append(cmdButton)
            print("Added draw command: {} ({})".format(cmdInstance.get_name(), cmdInstance.get_description()))

        self.commandButtons = []
        for command in commands:
            cmdButton = Button(self.topToolbar, image=self.res.get(command.get_id()), relief=FLAT)
            cmdHandler = partial(self.onDrawCommandButtonClick, cmdButton, command)
            cmdButton.config(command=cmdHandler)
            cmdButton.pack(side=LEFT, padx=2, pady=2)
            self.commandButtons.append(cmdButton)
            print("Added IO command: {} ({})".format(command.get_name(), command.get_description()))

        cmdColorPicker = Button(self.topToolbar, relief=RIDGE)
        cmdHandler = partial(self.onChangeColor, cmdColorPicker)
        cmdColorPicker.config(command=cmdHandler, background=self.colorPicker.getColor(), relief=GROOVE, width=2,
                              highlightbackground='white')
        cmdColorPicker.pack(side=LEFT, padx=15, pady=2)
        self.colorPickerButton = cmdColorPicker

    # Event handler when users change the selected color.
    def onChangeColor(self, button):
        self.colorPicker.selectColor(self.root)
        button.config(background=self.colorPicker.getColor())

    # Event handler when users click on a draw command button.
    def onDrawCommandButtonClick(self, button, command):
        # Reset relief state of other buttons
        for btn in self.commandButtons:
            if btn is not button:
                btn.config(relief=FLAT)

        # Set relief state for active command button
        button.config(relief=SUNKEN)
        self.onDrawCommandClick(button, command)
