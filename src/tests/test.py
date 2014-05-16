import unittest
from tkinter import Tk, Toplevel, Button, FLAT, SUNKEN, ALL

from controllers.commandstack import CommandStack
from controllers.drawcontroller import DrawController
from models.draw.circle import CircleDrawCommand
from models.io.undo import UndoDrawCommand
from models.io.redo import RedoDrawCommand
from models.io.new import NewDrawCommand
from drawings.canvas import DrawingCanvas
from views.gui import ClassicGUI
from tests.dummy import *
from models.draw.line import LineDrawCommand


class CommandStackTest(unittest.TestCase):
    """
    Unit Test for the command stack
    """

    def setUp(self):
        self.tk = Tk()

    def test_command_stack(self):
        """
        Test the operation of the command stack by try pushing new commands into the stack
        """
        commandStack = CommandStack()
        self.assertEquals(commandStack.can_undo(), False, "Empty command stack should not be undoable")
        self.assertEquals(commandStack.can_redo(), False, "Empty command stack should not be redoable")

        cmd = CircleDrawCommand()
        commandStack.add_command(cmd)
        self.assertEquals(commandStack.can_undo(), True, "Non-empty command stack should be undoable")
        self.assertEquals(commandStack.can_undo(), True, "Non-empty command stack should be redoable")

        colorPicker = ColorPicker(self.tk)
        canvas = DrawingCanvas(self.tk, colorPicker)
        tag = cmd.onDraw(canvas, 0, 0, 100, 100)
        commandStack.undo(canvas)
        self.assertEquals(canvas.getDrawArea().find_all().__len__(), 0, "The circle should be removed after undo")

        commandStack.redo(canvas)
        self.assertEquals(canvas.getDrawArea().find_all().__len__(), 1, "The circle should be added after redo")

        commandStack.clear()
        self.assertEquals(commandStack.can_undo(), False, "Empty command stack should not be undoable")
        self.assertEquals(commandStack.can_redo(), False, "Empty command stack should not be redoable")


    def test_gui(self):
        """
        The GUI interactions by simulating user actions
        """
        tl = Toplevel()
        gui = ClassicGUI(tl)
        gui.colorPicker = DummyColorPicker(tl)
        controller = DrawController(gui)
        self.assertEquals(gui.ioButtons.__len__(), 5, "There should be 5 IO buttons")
        self.assertEquals(gui.commandButtons.__len__(), 4, "There should be 4 draw command buttons")

        gui.onChangeColor(gui.colorPickerButton)
        self.assertEquals(gui.colorPickerButton.cget('bg'), gui.colorPicker.getColor())

        dummyButton = Button()
        gui.onDrawCommandButtonClick(dummyButton, LineDrawCommand)
        self.assertEquals(dummyButton.cget('relief'), SUNKEN, "Selected button should have style SUNKEN")

        for btn in gui.commandButtons:
            self.assertEquals(btn.cget('relief'), FLAT, "Selected button should have style FLAT")

        self.assertEquals(type(controller.activeCommand), LineDrawCommand, "Active command should be LineDrawCommand")

        for cmd in controller.commands:
            controller.canvas.getDrawArea().delete(ALL)
            self.assertCommandOperations(controller, cmd)

        clearCmd = NewDrawCommand()
        gui.onIOCommandClick(dummyButton, clearCmd)
        self.assertEquals(gui.canvas.getDrawArea().find_all().__len__(), 0,
                          "The canvas should be cleared on NewDrawCommand")


    def assertCommandOperations(self, controller, command):
        """
        Tests the command operation on GUI
        """
        gui = controller.view
        self.assertEquals(gui.canvas.getDrawArea().find_all().__len__(), 0,
                          "The canvas should be empty on initialization")

        oldCommand = controller.activeCommand
        dummyButton = Button()
        gui.onDrawCommandButtonClick(dummyButton, command)
        self.assertNotEqual(oldCommand, controller.activeCommand, "Command should be switched on button click")

        # Users click on the canvas
        controller.onStart(Mock(x=100, y=100))
        activeCommand = controller.activeCommand
        self.assertEquals(activeCommand.drawObject, None, "Drawn object should be reset on command start")
        self.assertEquals(activeCommand.fromX, 100, "Start point's X should be 100")
        self.assertEquals(activeCommand.fromY, 100, "Start point's Y should be 100")

        # Users drag the mouse to another point
        oldCommand = controller.activeCommand
        oldObject = oldCommand.drawObject
        controller.onDrag(Mock(x=150, y=150))
        self.assertEquals(controller.activeCommand, activeCommand,
                          "Active command should not be re-initialized on dragging")
        self.assertNotEqual(activeCommand.drawObject, None, "Drawn object should be set on dragging")
        self.assertNotEqual(activeCommand.drawObject, oldObject, "Drawn object should be re-drawn on dragging")
        self.assertEquals(activeCommand.fromX, 100, "Start point's X should be 100")
        self.assertEquals(activeCommand.fromY, 100, "Start point's Y should be 100")
        self.assertEquals(activeCommand.toX, 150, "End point's X should be 150")
        self.assertEquals(activeCommand.toY, 150, "End point's Y should be 150")
        self.assertEquals(gui.canvas.getDrawArea().find_all().__len__(), 1,
                          "The canvas should contain an object when dragging")
        oldObject = controller.activeCommand.drawObject

        # Users drag the mouse to another point again
        oldCommand = controller.activeCommand
        oldObject = oldCommand.drawObject
        controller.onDrag(Mock(x=500, y=1500))
        self.assertEquals(controller.activeCommand, activeCommand,
                          "Active command should not be re-initialized on dragging")
        self.assertNotEqual(activeCommand.drawObject, None, "Drawn object should be set on dragging")
        self.assertNotEqual(activeCommand.drawObject, oldObject, "Drawn object should be re-drawn on dragging")
        self.assertEquals(activeCommand.toX, 500, "End point's X should be 500")
        self.assertEquals(activeCommand.toY, 1500, "End point's Y should be 1500")
        self.assertNotEqual(activeCommand.drawObject, oldObject, "A new object should be drawn on dragging")

        # Users release the mouse
        oldCommand = controller.activeCommand
        oldObject = oldCommand.drawObject
        controller.onDragEnd(Mock(x=5000, y=2000))
        activeCommand = controller.activeCommand
        self.assertEqual(activeCommand.drawObject, None, "Drawn object should be reset on dragging")
        self.assertNotEqual(activeCommand, oldCommand, "New command instance should be initialized")
        self.assertEqual(type(activeCommand), type(oldCommand),
                         "New command instance should have the same type as the previous one")
        self.assertEquals(activeCommand.fromX, None, "Start point's X should be reset to None")
        self.assertEquals(activeCommand.fromY, None, "Start point's Y should be reset to None")
        self.assertEquals(activeCommand.toX, None, "End point's X should be reset to None")
        self.assertEquals(activeCommand.toY, None, "End point's Y should be reset to None")
        self.assertEquals(gui.canvas.getDrawArea().find_withtag(oldObject).__len__(), 1, "The object should be drawn")

        gui.onIOCommandClick(dummyButton, UndoDrawCommand())
        self.assertEquals(gui.canvas.getDrawArea().find_all().__len__(), 0, "The object should be deleted after undo")

        gui.onIOCommandClick(dummyButton, RedoDrawCommand())
        self.assertEquals(gui.canvas.getDrawArea().find_all().__len__(), 1,
                          "The same old object should be drawn after redo")


if __name__ == "__main__":
    unittest.main()