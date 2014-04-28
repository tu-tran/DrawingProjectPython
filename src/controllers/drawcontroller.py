from controllers.commandstack import CommandStack

from models.io.new import *
from models.io.open import *
from models.io.save import *

from models.draw.circle import *
from models.draw.line import *
from models.draw.oval import *
from models.draw.rectangle import *


class DrawController(object):
    """
    Draw controller responsble for connecting the GUI with the models
    """

    # Initialize a new instance of the controller
    def __init__(self, view):
        self.view = view
        self.canvas = view.canvas
        self.drawArea = view.canvas.getDrawArea()
        self.commandStack = CommandStack()
        self.view.canvas.bind('<ButtonPress-1>', self.onStart)
        self.view.canvas.bind('<B1-Motion>', self.onDrag)
        ios = [ NewDrawCommand, OpenDrawCommand, SaveDrawCommand ]
        commands = [ LineDrawCommand, RectangleDrawCommand, CircleDrawCommand, OvalDrawCommand ]
        self.view.onIOCommandClick = self.onIOCommandClick
        self.view.onDrawCommandClick = self.onDrawCommandClick
        self.view.initButtons(ios, commands)
        self.activeCommand = LineDrawCommand()

    def onStart(self, event):
        self.startX = self.drawArea.canvasx(event.x)
        self.startY = self.drawArea.canvasy(event.y)
        self.drawObject = None

    def onDrag(self, event):
        canvas = event.widget
        if self.drawObject:
            self.drawArea.delete(self.drawObject)
        self.drawObject = self.activeCommand.draw(self.canvas, self.startX, self.startY, self.drawArea.canvasx(event.x),
                                   self.drawArea.canvasy(event.y))

    def onIOCommandClick(self, command):
        print("Activated IO command: " + command.__name__)
        command().execute(self.canvas)

    def onDrawCommandClick(self, command):
        print("Changed active command: " + command.__name__)
        self.activeCommand = command()
