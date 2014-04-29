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
        '''
        Tests if an undo operation can be performed at this moment.
        
        @return: boolean value telling if an undo is possible to perform.
        '''
        if self.undo_stack:
            return True
        return False


    def can_redo(self):
        '''
        Tests if an redo operation can be performed at this moment.
        
        @return: boolean value telling if a redo is possible to perform.
        '''
        if self.redo_stack:
            return True
        return False


    def add_command(self, command):
        '''
        Adds a new undoable command into this Undo Manager.
        
        @param command: the Undoablecommand to be added.
        '''
        self.redo_stack = []
        self.undo_stack.append(command)

    def undo(self, canvas):
        '''
        Undoes one command from the undo stack. The undone command then is moved to
        the redo stack.
        '''
        command = self.undo_stack.pop()
        command.undo(canvas)
        self.redo_stack.append(command)

    def redo(self, canvas):
        '''
        Redoes one command from the redo stack. The redone command then is moved to
        the undo stack.
        '''
        command = self.redo_stack.pop()
        command.execute(canvas)
        self.undo_stack.append(command)


    def describe_undoable_command(self):
        '''
        Describes an available undoable command.
        
        @return: A description of the undoable command for menus etc.
        '''
        if self.can_undo():
            return "Undo " + self.undo_stack[-1].get_description()
        return "Nothing to undo."


    def describe_redoable_command(self):
        '''
        Describes an available redoable command.
        
        @return: A description of the redoable command for menus etc.
        '''
        if self.can_redo():
            return "Redo " + self.redo_stack[-1].get_description()
        return "Nothing to redo."
