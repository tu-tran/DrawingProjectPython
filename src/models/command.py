from abc import ABCMeta, abstractmethod


class Command(object):
    """
    Base abstract class for all commands
    """

    __metaclass__ = ABCMeta

    #Get unique command ID
    @staticmethod
    @abstractmethod
    def get_id():
        pass

    # Get the name of the command
    @staticmethod
    @abstractmethod
    def get_name():
        pass

    # Get the description of the command
    @staticmethod
    @abstractmethod
    def get_description():
        pass