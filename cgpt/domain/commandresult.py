class CommandResult:
    """
    A class to represent the result of a command.
    """

    def __init__(self, success, commands, description, is_dangerous):
        """
        Initialize a new CommandResult object.

        :param success: A boolean indicating whether the command was successful.
        :param commands: A string or list of strings representing the commands that were executed.
        :param description: A string describing the command or commands that were executed.
        :param is_dangerous: A boolean indicating whether the command is dangerous.
        """
        self.success = success
        self.commands = commands
        self.description = description
        self.is_dangerous = is_dangerous