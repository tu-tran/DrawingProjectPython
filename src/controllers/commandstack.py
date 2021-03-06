class CommandStack(object):
    """
    CommandStack is used to support an undo-redo mechanism.
    """


    def __init__(self):
        # Undo and redo stacks which contain the Undoablecommand objects
        # When a new command is made it is put in the undo stack. When an operation
        # is undone, it is places in the redo stack.
        self.undo_stack = []
        self.redo_stack = []


    def can_undo(self):
        """
        Tests if an undo operation can be performed at this moment.

        @return: boolean value telling if an undo is possible to perform.
        """
        if self.undo_stack:
            return True
        return False


    def can_redo(self):
        """
        Tests if an redo operation can be performed at this moment.

        @return: boolean value telling if a redo is possible to perform.
        """
        if self.redo_stack:
            return True
        return False


    def clear(self):
        self.redo_stack = []
        self.undo_stack = []


    def add_command(self, command):
        """
        Adds a new undoable command into this Undo Manager.
        
        @param command: the Undoablecommand to be added.
        """
        self.redo_stack = []
        self.undo_stack.append(command)

    def undo(self, canvas):
        """
        Undoes one command from the undo stack. The undone command then is moved to
        the redo stack.
        """
        if self.can_undo():
            command = self.undo_stack.pop()
            command.undo(canvas)
            self.redo_stack.append(command)

    def redo(self, canvas):
        """
        Redoes one command from the redo stack. The redone command then is moved to
        the undo stack.
        """
        if self.can_redo():
            command = self.redo_stack.pop()
            command.redo(canvas)
            self.undo_stack.append(command)