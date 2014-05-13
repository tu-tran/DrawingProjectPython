from tkinter import Canvas
from src.views.resourcemanager import ResourceManager

from src.models.drawcommand import DrawCommand


class RectangleDrawCommand(DrawCommand):
    """
    Command for drawing a rectangle (box)
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.RECTANGLE

    # Get the name of the command
    @staticmethod
    def get_name():
        return "Draw Rectangle"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Draw a rectangle between two points"

    # Draw a rectangle between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        return Canvas.create_rectangle(canvas.getDrawArea(),
                                       fromX,
                                       fromY,
                                       toX,
                                       toY,
                                       outline=canvas.getShapeColor(), width=self.PEN_WIDTH)