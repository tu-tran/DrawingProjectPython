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
        self.ios = [NewDrawCommand,
                    OpenDrawCommand,
                    SaveDrawCommand,
                    UndoDrawCommand,
                    RedoDrawCommand]

        self.commands = [LineDrawCommand,
                         RectangleDrawCommand,
                         CircleDrawCommand,
                         OvalDrawCommand]

        self.view.onIOCommandClick = self.onIOCommandClick
        self.view.onDrawCommandClick = self.onDrawCommandClick
        self.view.initButtons(self.ios, self.commands)

    def onStart(self, event):
        """
        Event handler when users pick the first point on the drawing canvas
        """
        if self.activeCommand:
            self.activeCommand.fromX = self.drawArea.canvasx(event.x)
            self.activeCommand.fromY = self.drawArea.canvasy(event.y)
            self.activeCommand.drawObject = None

    def onDrag(self, event):
        """
        Event handler when users drag the mouse when creating a new shape on the drawing canvas
        """
        if self.activeCommand:
            if self.activeCommand.drawObject:
                self.drawArea.delete(self.activeCommand.drawObject)
            self.activeCommand.onDraw(self.canvas, self.activeCommand.fromX, self.activeCommand.fromY,
                                      self.drawArea.canvasx(event.x),
                                      self.drawArea.canvasy(event.y))

    def onDragEnd(self, event):
        """
        Event handler when users release the mouse when creating a new shape on the drawing canvas
        """
        if self.activeCommand:
            print("Drew object: " + str(self.activeCommand.drawObject))
            self.commandStack.add_command(self.activeCommand)
            self.activeCommand = type(self.activeCommand)()

    def onIOCommandClick(self, button, command):
        """
        Event handler when users click on an IO command (e.g. clear, open, save)
        """
        print("Activated IO command: " + command.get_name())
        command.execute(self.canvas, self.commandStack)

    def onDrawCommandClick(self, button, command):
        """
        Event handler when users click on a Draw command (e.g. select shape type)
        """
        print("Changed active command: " + command.__name__)
        self.activeCommand = command()
