from controllers.commandstack import CommandStack

from models.io.new import *
from models.io.open import *
from models.io.save import *
from models.io.undo import *
from models.io.redo import *

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
        self.activeCommand = None
        self.view.canvas.bind('<ButtonPress-1>', self.onStart)
        self.view.canvas.bind('<B1-Motion>', self.onDrag)
        self.view.canvas.bind('<ButtonRelease-1>', self.onDragEnd)
        ios = [ NewDrawCommand,
				OpenDrawCommand,
				SaveDrawCommand,
				UndoDrawCommand,
				RedoDrawCommand ]
				
        commands = [ LineDrawCommand,
					 RectangleDrawCommand, 
					 CircleDrawCommand, 
					 OvalDrawCommand ]
					 
        self.view.onIOCommandClick = self.onIOCommandClick
        self.view.onDrawCommandClick = self.onDrawCommandClick
        self.view.initButtons(ios, commands)

    def onStart(self, event):
        if self.activeCommand:
            self.startX = self.drawArea.canvasx(event.x)
            self.startY = self.drawArea.canvasy(event.y)
            self.drawObject = None

    def onDrag(self, event):
        if self.activeCommand:
            canvas = event.widget
            if self.drawObject:
                self.drawArea.delete(self.drawObject)
            self.drawObject = self.activeCommand.onDraw(self.canvas, self.startX, self.startY, self.drawArea.canvasx(event.x),
                                       self.drawArea.canvasy(event.y))

    def onDragEnd(self, event):
        if self.activeCommand:
            print("Drew object: " + str(self.drawObject))
            self.commandStack.add_command(self.activeCommand)
            self.activeCommand = type(self.activeCommand)()

    def onIOCommandClick(self, button, command):
        print("Activated IO command: " + command.get_name())
        command.execute(self.canvas, self.commandStack)

    def onDrawCommandClick(self, button, command):
        print("Changed active command: " + command.__name__)
        self.activeCommand = command()
