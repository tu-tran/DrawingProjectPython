from models.command import Command

class IOCommand(Command):
    """
    IO commands such as opening/saving Bitmap files
    """

    FILE_TYPE = [('Bitmap Image', '*.bmp'), ('All files', '*')]
    FILE_EXTENSION = '.bmp'
	
    def execute(self, canvas, commandStack):
        pass