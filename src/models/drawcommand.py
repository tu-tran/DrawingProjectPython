from models.command import Command

class DrawCommand(Command):
    """
    Base abstract class for all drawing commands
    """

    #Draw a graphic between two points
    def draw(self, canvas, fromX, fromY, toX, toY):
        pass