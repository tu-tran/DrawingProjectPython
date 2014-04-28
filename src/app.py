"""
Title: Drawing program (topic #151)
Student name: Tu Tran Le
Student number: 401311
Study program: Service Design and Engineering
"""

from tkinter import Tk
from drawings.canvas import *
from drawings.colorpicker import ColorPicker
from views.gui import ClassicGUI
from controllers.drawcontroller import DrawController

class DrawingApp:
    """
    Main entry point application
    """

    def __init__(self):
        self.root = Tk()
        self.root.title('Topic 15: Drawing Project - Tu Tran Le - 401311')
        self.root.protocol('WM_DELETE_WINDOW', self.onQuit)
        self.gui = ClassicGUI(self.root)
        self.controller = DrawController(self.gui)


    def start(self):
        self.root.mainloop()


    def onClear(self, event):
        if self.moving: return # ok if moving but confusing
        event.widget.delete('all')   # use all tag
        self.images = []
        self.textInfo = self.canvas.create_text(
            5, 5, anchor=NW,
            text='Press ? for help')

    def onQuit(self):
        self.root.quit()
        exit()
        if self.canvas.isModified:
            return
        else:
            self.appExit()


if __name__ == '__main__':
    app = DrawingApp()
    app.start()
    exit()