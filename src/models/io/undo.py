from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class UndoDrawCommand(IOCommand):
    """
    Command for undoing last command
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.UNDO

    # Get the name of the command
    @staticmethod
    def get_name():
        return "Undo"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Undo last command"

    # Undo previous command
    def execute(self, canvas, commandStack):
        commandStack.undo(canvas)
