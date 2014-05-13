from tkinter import Canvas
from src.views.resourcemanager import ResourceManager

from src.models.drawcommand import DrawCommand


class OvalDrawCommand(DrawCommand):
    """
    Command for drawing an oval
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.OVAL

    # Get the name of the command
    @staticmethod
    def get_name():
        return "Draw Circle"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Draw a circle between two points"

    # Draw an oval between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        return Canvas.create_oval(canvas.getDrawArea(), fromX, fromY, toX, toY, outline=canvas.getShapeColor(),
                                  width=self.PEN_WIDTH)