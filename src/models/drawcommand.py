from abc import ABCMeta, abstractmethod
from src.models.command import Command


class DrawCommand(Command):
    """
    Base abstract class for all drawing commands
    """

    __metaclass__ = ABCMeta
    PEN_WIDTH = 2
    drawObject = None

    def __init__(self):
        self.fromX = None
        self.fromY = None
        self.toX = None
        self.toY = None

    #Event handler when users want to draw a graphic between two points.
    def onDraw(self, canvas, fromX, fromY, toX, toY):
        self.drawObject = self.draw(canvas, fromX, fromY, toX, toY)
        self.fromX = fromX
        self.fromY = fromY
        self.toX = toX
        self.toY = toY

        return self.drawObject

    #Abstract method to actually draw a graphic between two points.
    #The function returns the drawn object id.
    @abstractmethod
    def draw(self, canvas, fromX, fromY, toX, toY):
        pass

    #Undo the previous draw command.
    def undo(self, canvas):
        print("Delete drawn object: " + str(self.drawObject))
        canvas.getDrawArea().delete(self.drawObject)
        self.drawObject = None

    #Redo the previous draw command.
    def redo(self, canvas):
        self.drawObject = self.draw(canvas, self.fromX, self.fromY, self.toX, self.toY)