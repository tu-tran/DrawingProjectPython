from models.command import Command

class DrawCommand(Command):
    """
    Base abstract class for all drawing commands
    """
	
    #Draw a graphic between two points
    def onDraw(self, canvas, fromX, fromY, toX, toY):
        self.drawObject = self.draw(canvas, fromX, fromY, toX, toY)
        self.fromX = fromX
        self.fromY = fromY
        self.toX = toX
        self.toY = toY

        return self.drawObject

    #Draw a graphic between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        pass

    #Undo the previous draw command
    def undo(self, canvas):
        print("Delete drawn object")
        canvas.getDrawArea().delete(self.drawObject)
        self.drawObject = None
		
    #Redo the previous draw command
    def redo(self, canvas):
        self.drawObject = self.draw(canvas, self.fromX, self.fromY, self.toX, self.toY)