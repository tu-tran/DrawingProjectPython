from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class RedoDrawCommand(IOCommand):
    """
    Command for redoing last command
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.REDO

    # Get the name of the command
    def get_name(self):
        return "Redo"

    # Get the description of the command
    def get_description(self):
        return "Redo last command"

    # Redo last command
    def execute(self, canvas, commandStack):
        commandStack.redo(canvas)
