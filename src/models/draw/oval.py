from tkinter import Canvas
from views.resourcemanager import ResourceManager

from models.drawcommand import DrawCommand


class OvalDrawCommand(DrawCommand):
    """
    Command for drawing an oval
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.OVAL

    # Get the name of the command
    def get_name(self):
        return "Draw Circle"

    # Get the description of the command
    def get_description(self):
        return "Draw a circle between two points"

    # Draw an oval between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        return Canvas.create_oval(canvas.getDrawArea(), fromX, fromY, toX, toY, outline=canvas.getShapeColor(),
                                  width=self.PEN_WIDTH)