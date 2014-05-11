from tkinter import Canvas
from views.resourcemanager import ResourceManager
from models.drawcommand import DrawCommand


class CircleDrawCommand(DrawCommand):
    """
    Command for drawing a circle
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.CIRCLE

    # Get the name of the command
    def get_name(self):
        return "Draw Circle"

    # Get the description of the command
    def get_description(self):
        return "Draw a circle between two points"

    # Draw a circle between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        xLen = abs(toX - fromX)
        yLen = abs(toY - fromY)
        diameter = xLen if xLen > yLen else yLen
        xFactor = 1 if toX > fromX else -1
        yFactor = 1 if toY > fromY else -1
        return Canvas.create_oval(canvas.getDrawArea(),
                                  fromX,
                                  fromY,
                                  fromX + xFactor * diameter,
                                  fromY + yFactor * diameter,
                                  outline=canvas.getShapeColor(), width=self.PEN_WIDTH)