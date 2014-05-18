"""
Title: Drawing program (topic #151)
Student name: Tu Tran Le
Student number: 401311
Study program: Service Design and Engineering
"""

from drawings.canvas import *
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


    def onQuit(self):
        self.root.quit()
        exit()


if __name__ == '__main__':
    app = DrawingApp()
    app.start()
    exit()
