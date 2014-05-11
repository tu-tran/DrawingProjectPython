from models.command import Command


class IOCommand(Command):
    """
    IO commands such as opening/saving Bitmap files
    """

    FILE_TYPE = [('Bitmap Image', '*.bmp'), ('All files', '*')]
    FILE_EXTENSION = '.bmp'

    # Executes the IO command. The function takes the drawing canvas and the command stack as input parameters.
    def execute(self, canvas, commandStack):
        pass