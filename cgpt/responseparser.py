import json
from domain.commandresult import CommandResult


class ResponseParser:
    @staticmethod
    def parse_gpt_command(response):
        """
        Parse the JSON response returned by the OpenAI GPT-3 API.

        :param response: The JSON response as a string.
        :return: A dictionary containing the command result.
        """

        try:
            # Parse the JSON string into a Python dictionary
            response_dict = json.loads(response)
        except json.JSONDecodeError:
            print(response)
            print("Failed to parse the response.")
            return None

        try:
            # Extract the command result from the dictionary
            success = response_dict.get("success", False)
            commands = response_dict.get("commands", [])
            description = response_dict.get("description", "")
            is_dangerous = response_dict.get("isDangerous", False)
        except KeyError as e:
            print(f"Failed to extract key from the response: {e}")
            return None

        try:
            command_result = CommandResult(
                success=success,
                command_text=commands,
                commands=ResponseParser.parse_commands_text(commands),
                description=description,
                is_dangerous=is_dangerous
            )
        except Exception as e:
            print(f"Failed to create CommandResult: {e}")
            return None

        return command_result
        

    @staticmethod
    def parse_commands_text(commands_text):
        """
        Parse the commands text returned by the OpenAI GPT-3 API.

        :param commands_text: The commands text as a string.
        :return: A list of strings representing the commands.
        """
        # Split the commands text into a list of strings
        commands = commands_text.split("\n")

        # Remove any empty strings from the list
        commands = list(filter(None, commands))

        return commands
