from tkinter import ALL
from src.drawings.canvas import DrawingCanvas
from src.views.resourcemanager import ResourceManager
from src.models.iocommand import IOCommand


class NewDrawCommand(IOCommand):
    """
    Command for creating a new drawing
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.NEW_DRAWING

    # Get the name of the command
    @staticmethod
    def get_name():
        return "New Drawing"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Create a new drawing"

    # Create a new drawing
    def execute(self, canvas, commandStack):
        canvas.getDrawArea().delete(ALL)
        canvas.getDrawArea().config(width=DrawingCanvas.DEFAULT_WIDTH, height=DrawingCanvas.DEFAULT_HEIGHT)
        commandStack.clear()
