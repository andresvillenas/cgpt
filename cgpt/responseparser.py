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
            response_dict = json.loads(response, strict=False)
        except json.JSONDecodeError as e:
            print(f"\nFailed to parse the response: {response}")
            print(f"Error: {e}")
            return None

        try:
            # Extract the command result from the dictionary
            success = response_dict.get("success", False)
            commands = response_dict.get("commands", "")
            explanation = response_dict.get("explanation", None)
            is_dangerous = response_dict.get("isDangerous", False)
        except KeyError as e:
            print(f"Failed to extract key from the response: {e}, response: {response}")
            return None

        try:
            command_result = CommandResult(
                success=success,
                command_text=ResponseParser.parse_commands_text(commands),
                commands=commands,
                explanation=explanation,
                is_dangerous=is_dangerous
            )
        except Exception as e:
            print(f"Failed to create CommandResult: {e}, response: {response}")
            return None

        return command_result
        

    @staticmethod
    def parse_commands_text(commands):
        trimmed_commands = [command.strip() for command in commands if command.strip()]
        commands_text = "\n".join(trimmed_commands)
        return commands_text
