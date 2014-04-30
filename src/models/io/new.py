from tkinter import ALL
from drawings.canvas import DrawingCanvas
from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class NewDrawCommand(IOCommand):
    """
    Command for creating a new drawing
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.NEW_DRAWING

    # Get the name of the command
    def get_name(self):
        return "New Drawing"

    # Get the description of the command
    def get_description(self):
        return "Create a new drawing"

    # Create a new drawing
    def execute(self, canvas):
        canvas.getDrawArea().delete(ALL)
        canvas.getDrawArea().config(width=DrawingCanvas.DEFAULT_WIDTH, height=DrawingCanvas.DEFAULT_HEIGHT)
