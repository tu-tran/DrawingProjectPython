class Command(object):
    """
    Base abstract class for all commands
    """

    #Get unique command ID
    @staticmethod
    def getId():
        pass

    # Get the name of the command
    def get_name(self):
        pass

    # Get the description of the command
    def get_description(self):
        pass