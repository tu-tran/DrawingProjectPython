import os
from tkinter import PhotoImage
from abc import ABCMeta, abstractmethod


class ResourceManager(object):
    """
    Utility base class for retrieving program resources. Current this class only handles image resources.
    """

    __metaclass__ = ABCMeta

    # Constants for defining unique resource ID.
    EXIT = "prog_exit"
    NEW_DRAWING = "io_new"
    OPEN_DRAWING = "io_open"
    SAVE_DRAWING = "io_save"
    UNDO = "io_undo"
    REDO = "io_redo"

    LINE = "cmd_line"
    RECTANGLE = "cmd_rect"
    OVAL = "cmd_oval"
    CIRCLE = "cmd_circle"

    @abstractmethod
    def get(self, name):
        pass


class DefaultResourceManager(ResourceManager):
    """
    Default resource manager
    """
    BASE_PATH = os.path.dirname(os.path.realpath(__file__)) + "/res/default/"
    data = {
        ResourceManager.NEW_DRAWING: [BASE_PATH + "new.png", None],
        ResourceManager.OPEN_DRAWING: [BASE_PATH + "open.png", None],
        ResourceManager.SAVE_DRAWING: [BASE_PATH + "save.png", None],
        ResourceManager.UNDO: [BASE_PATH + "undo.png", None],
        ResourceManager.REDO: [BASE_PATH + "redo.png", None],

        ResourceManager.LINE: [BASE_PATH + "line.png", None],
        ResourceManager.RECTANGLE: [BASE_PATH + "rect.png", None],
        ResourceManager.OVAL: [BASE_PATH + "oval.png", None],
        ResourceManager.CIRCLE: [BASE_PATH + "circle.png", None]
    }

    # Initialize a new instance of the default resource manager
    def __init__(self):
        for (k, v) in self.data.items():
            v[1] = PhotoImage(file=v[0])


    # Get the resource associated with certain name
    def get(self, name):
        d = self.data[name]
        if d is None or d[1] is None:
            return None

        img = d[1]
        return img
