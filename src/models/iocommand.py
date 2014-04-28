from models.command import Command

class IOCommand(Command):
    """
    IO commands such as opening/saving Bitmap files
    """

    FILE_TYPE = [('All files', '*')]
    FILE_EXTENSION = ''

    def execute(self, canvas):
        pass