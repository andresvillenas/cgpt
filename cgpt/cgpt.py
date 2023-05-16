import os
import argparse

from halo import Halo
from responseparser import ResponseParser
from gptservice import GptService
from config.settings import Config
from promptservice import PromptService

config = Config()


def get_commands(user_input, gptService, prompt_service, response_parser):
    with Halo(text='Generating command', spinner="dots2", color="white", placement="right", animation="bounce"):
        prompt = prompt_service.load_prompt(user_input=user_input)
        response = gptService.get_response(prompt)
        commandresult = response_parser.parse_gpt_command(response)
        return commandresult


def execute_commands(commandresult, explain=False):
    if explain:
        print(commandresult.description)

    if commandresult.is_dangerous:
        print("⚠️ Warning: This command is dangerous and may cause harm to your system. Please use with caution.")

    print(f"\nCommand: {commandresult.command_text}")

    confirm = input("Do you want to proceed? (yes/no): ")
    if confirm.lower() in ["yes", "y"]:
        for command in commandresult.commands:
            print(f"\nExecuting command: {command}")
            os.system(command)
    else:
        print("Command not executed.")


def main(user_input, explain):
    # Initialize services
    gptService = GptService()
    prompt_service = PromptService(
        config.prompts.prompts_folder, config.prompts.default_prompt_file)
    response_parser = ResponseParser()

    commandresult = get_commands(
        user_input, gptService, prompt_service, response_parser)

    execute_commands(commandresult, explain)


# Set up the command line argument parser
parser = argparse.ArgumentParser(description="cgpt - Command GPT")
parser.add_argument("-i", "--input", type=str,
                    required=True, help="The user input command")
parser.add_argument("-e", "--explain", action='store_true',
                    required=False, help="To explain the command")

# Parse the command line arguments
args = parser.parse_args()

if __name__ == "__main__":
    main(user_input=args.input, explain=args.explain)
