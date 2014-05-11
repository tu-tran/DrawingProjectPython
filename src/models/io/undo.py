from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class UndoDrawCommand(IOCommand):
    """
    Command for undoing last command
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.UNDO

    # Get the name of the command
    def get_name(self):
        return "Undo"

    # Get the description of the command
    def get_description(self):
        return "Undo last command"

    # Undo previous command
    def execute(self, canvas, commandStack):
        commandStack.undo(canvas)
