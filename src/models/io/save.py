from tkinter.filedialog import asksaveasfilename
from views.resourcemanager import ResourceManager
from models.iocommand import IOCommand


class SaveDrawCommand(IOCommand):
    """
    Command for creating a new drawing
    """

    #Get unique command ID
    @staticmethod
    def get_id():
        return ResourceManager.SAVE_DRAWING

    # Get the name of the command
    @staticmethod
    def get_name():
        return "Save Drawing"

    # Get the description of the command
    @staticmethod
    def get_description():
        return "Save a drawing"

    # Save a drawing
    def execute(self, canvas, commandStack):
        fileName = asksaveasfilename(filetypes=self.FILE_TYPE, defaultextension=self.FILE_EXTENSION)
        if fileName:
            canvas.getDrawArea().update()
            import uuid
            from PIL import Image

            tempFile = uuid.uuid1().hex
            canvas.getDrawArea().postscript(file=tempFile, colormode="color")

            with open(str(tempFile), 'rb') as f:
                try:
                    img = Image.open(tempFile)
                    img.save(fileName, "bmp")
                except Exception as ex:
                    print("Failed to save file {}: {}".format(str(fileName), str(ex)))
                del img

            import os
            os.remove(tempFile)
            commandStack.clear()