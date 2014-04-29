from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class RedoDrawCommand(IOCommand):
    """
    Command for redoing last command
    """
    
    def __init__(self, commandStack):
        self.commandStack = commandStack

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.NEW_DRAWING

    # Get the name of the command
    def get_name(self):
        return "Redo"

    # Get the description of the command
    def get_description(self):
        return "Redo last command"

    # Redo last command
    def execute(self, canvas):
        self.commandStack.redo(canvas)
