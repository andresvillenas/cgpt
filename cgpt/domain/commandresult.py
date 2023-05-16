class CommandResult:
    """
    A class to represent the result of a command.
    """

    def __init__(self, success, command_text, commands, description, is_dangerous):
        """
        Initialize a new CommandResult object.

        :param success: A boolean indicating whether the command was successful.
        :param command_text: A string representing the command text that was executed.
        :param commands: A string or list of strings representing the commands that were executed.
        :param description: A string describing the command or commands that were executed.
        :param is_dangerous: A boolean indicating whether the command is dangerous.
        """
        self.success = success
        self.command_text = command_text
        self.commands = commands
        self.description = description
        self.is_dangerous = is_dangerous