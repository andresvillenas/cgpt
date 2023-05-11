import os
import openai
import json
import argparse
import sys

from halo import Halo

from domain.commandresult import CommandResult
from config.settings import Config

config = Config()

openai.api_key = config.openai.api_key

prompts_folder = "prompts"
default_prompt_file = "default.prmp"

def load_prompt(prompt_file=default_prompt_file, **kwargs):
    """
    Load the prompt from a file and replace placeholders with values.

    :param prompt_file: The name of the file containing the prompt.
    :param kwargs: Any keyword arguments representing placeholders and their values.
    :return: The prompt as a string with placeholders replaced by values.
    """

    # Get the path to the prompts directory
    if getattr(sys, 'frozen', False):
        # If running from a standalone executable, use the _MEIPASS directory
        prompts_folder = os.path.join(sys._MEIPASS, 'prompts')
    else:
        # If running from a development environment, use the prompts directory in the current directory
        prompts_folder = os.path.join(os.path.dirname(__file__), 'prompts')

    # Construct the full path to the prompt file
    prompt_path = os.path.join(prompts_folder, prompt_file)

    # Read the prompt from the file
    with open(prompt_path, "r") as f:
        prompt = f.read()

    # Replace any placeholders with values
    for key, value in kwargs.items():
        placeholder = "{" + key + "}"
        prompt = prompt.replace(placeholder, value)

    return prompt


def get_gpt3_response(user_input, os_name):
    # Construct the prompt
    prompt = load_prompt(user_input=user_input, os_name=os_name)

    # Get the response from GPT-3
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.5,
      max_tokens=100
    )

    return response.choices[0].text.strip()

def parse_gpt3_response(response):
    """
    Parse the JSON response returned by the OpenAI GPT-3 API.

    :param response: The JSON response as a string.
    :return: A dictionary containing the command result.
    """
    # Parse the JSON string into a Python dictionary
    response_dict = json.loads(response)

    # Extract the command result from the dictionary
    success = response_dict["success"]
    commands = response_dict["commands"]
    description = response_dict["description"]
    is_dangerous = response_dict["isDangerous"]

    command_result = CommandResult(
        success=success,
        commands=parse_commands_text(commands),
        description=description,
        is_dangerous=is_dangerous
    )   

    return command_result

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


def main(user_input):
    os_name = 'Windows' if os.name == 'nt' else 'Linux'

    commands = []

    with Halo(text='Generating command', spinner="dots2", color="white", placement="right", animation="bounce"):
        response = get_gpt3_response(user_input, os_name)
        commandresult = parse_gpt3_response(response)
        commands = commandresult.commands

    for command in commands:
        print(f"\nExecuting command: {command}")
        os.system(command)

# Set up the command line argument parser
parser = argparse.ArgumentParser(description="Command-line interface for expert OS commands")
parser.add_argument("-i", "--input", type=str, required=True, help="The user input command")

# Parse the command line arguments
args = parser.parse_args()


if __name__ == "__main__":
    main(user_input=args.input)
