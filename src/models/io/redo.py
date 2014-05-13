from src.views.resourcemanager import ResourceManager
from src.models.iocommand import IOCommand


class RedoDrawCommand(IOCommand):
    """
    Command for redoing last command
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.REDO

    # Get the name of the command
    @staticmethod
    def get_name():
        return "Redo"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Redo last command"

    # Redo last command
    def execute(self, canvas, commandStack):
        commandStack.redo(canvas)
