from tkinter import BitmapImage
from tkinter.filedialog import askopenfilename
from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class OpenDrawCommand(IOCommand):
    """
    Command for creating a new drawing
    """

    #Get unique command ID
    @staticmethod
    def getId():
        return ResourceManager.OPEN_DRAWING

    # Get the name of the command
    def get_name(self):
        return "Open Drawing"

    # Get the description of the command
    def get_description(self):
        return "Open an existing drawing"

    # Open an existing drawing
    def execute(self, canvas):
        fileName = askopenfilename(filetypes=self.FILE_TYPE, defaultextension=self.FILE_EXTENSION)
        if fileName:
            image = BitmapImage(file=fileName)                       # load image
            self.object = canvas.getDrawArea().create_image(# add to canvas
                                                            0, 0,
                                                            bitmap=image)
