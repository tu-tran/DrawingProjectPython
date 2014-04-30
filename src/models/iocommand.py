from models.command import Command

class IOCommand(Command):
    """
    IO commands such as opening/saving Bitmap files
    """

    FILE_TYPE = [('Bitmap Image', '*.bmp'), ('All files', '*')]
    FILE_EXTENSION = '.bmp'
	
    def __init__(self, canvas):
        self.canvas = canvas

    def execute(self, canvas):
        pass