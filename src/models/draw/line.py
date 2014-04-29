from tkinter import Canvas
from views.resourcemanager import ResourceManager
from models.drawcommand import DrawCommand


class LineDrawCommand(DrawCommand):
    """
    Command for drawing a straight line
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.LINE

    # Get the name of the command
    def get_name(self):
        return "Draw Line"

    # Get the description of the command
    def get_description(self):
        return "Draw a straight line between two points"

    # Draw a straight line between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        return Canvas.create_line(canvas.getDrawArea(),
                           fromX,
                           fromY,
                           toX,
                           toY,
                           fill=canvas.getShapeColor())