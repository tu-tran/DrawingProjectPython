from models.command import Command

class IOCommand(Command):
    """
    IO commands such as opening/saving Bitmap files
    """

    FILE_TYPE = [('All files', '*')]
    FILE_EXTENSION = ''
	
    def __init__(self, canvas):
        self.canvas = canvas

    def execute(self, canvas):
        pass