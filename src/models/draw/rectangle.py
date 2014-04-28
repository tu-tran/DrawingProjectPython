from tkinter import Canvas
from views.resourcemanager import ResourceManager

from models.drawcommand import DrawCommand


class RectangleDrawCommand(DrawCommand):
    """
    Command for drawing a rectangle (box)
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.RECTANGLE

    # Get the name of the command
    def get_name(self):
        return "Draw Rectangle"

    # Get the description of the command
    def get_description(self):
        return "Draw a rectangle between two points"

    # Draw a rectangle between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        return Canvas.create_rectangle(canvas.getDrawArea(),
                                fromX,
                                fromY,
                                toX,
                                toY,
                                outline=canvas.getShapeColor())