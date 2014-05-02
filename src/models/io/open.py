from tkinter import BitmapImage, ALL, NW
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
    def execute(self, canvas, commandStack):
        fileName = askopenfilename(filetypes=self.FILE_TYPE, defaultextension=self.FILE_EXTENSION)
        if fileName:
            from PIL import Image, ImageTk
            image = Image.open(fileName)				# load image
            photoImg = ImageTk.PhotoImage(image)
            print("Opening image {}: {}x{}".format(fileName, photoImg.width(), photoImg.height()))
            canvas.getDrawArea().delete(ALL)
            canvas.getDrawArea().config(width=photoImg.width(), height=photoImg.height())
            self.object = canvas.getDrawArea().create_image(0, 0, image=photoImg, anchor=NW)
            self.photoImg = photoImg
            commandStack.clear()
