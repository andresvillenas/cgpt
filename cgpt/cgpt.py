import argparse
import subprocess

from halo import Halo
from responseparser import ResponseParser
from gptservice import GptService
from config.settings import Config
from promptservice import PromptService

config = Config()


def get_commands(user_input, explain, gptService, prompt_service, response_parser):
    with Halo(text='Generating command', spinner="dots2", color="white", placement="right", animation="bounce"):
        prompt = prompt_service.load_prompt(user_input=user_input, include_explanation=explain)
        response = gptService.get_response(prompt)
        commandresult = response_parser.parse_gpt_command(response)
        return commandresult


def execute_commands(commandresult):
    if commandresult.is_dangerous:
        print("⚠️  Warning: This command is dangerous and may cause harm to your system. Please use with caution.")

    print(f"Command(s) generated:\n{commandresult.command_text}")
    if commandresult.explanation is not None :
        print(f"\n🏫  Explanation:\n{commandresult.explanation}")

    confirm = input("\nDo you want to proceed? (yes/no): ")
    if confirm.lower() in ["yes", "y"]:
        process = subprocess.Popen(" && ".join(commandresult.commands), shell=True)
        process.wait()
        if process.returncode != 0:
            print(f"❌  Command(s) failed with return code: {process.returncode}")
            print("Execution aborted.")
            return
        else:
            print("✅  Commands executed successfully.")
    else:
        print("Command not executed.")


def main(user_input, explain):
    # Initialize services
    gptService = GptService()
    prompt_service = PromptService(
        config.prompts.prompts_folder, config.prompts.default_prompt_file)
    response_parser = ResponseParser()

    commandresult = get_commands(user_input, explain, gptService, prompt_service, response_parser)

    if commandresult is not None:
        execute_commands(commandresult)
    else:
        print("Command not executed.")

# Set up the command line argument parser
parser = argparse.ArgumentParser(description="cgpt - Command GPT")

# Add the positional argument for input without specifying any flags
parser.add_argument("input", nargs="+", type=str, help="The user input command")

# Add the optional -e flag for explanation
parser.add_argument("-e", "--explain", action='store_true', help="To explain the command")

# Parse the command line arguments
args = parser.parse_args()

# Check if the -e flag is provided
is_explain_mode = args.explain

# Access the value of the input as a single string
user_input = " ".join(args.input)

if __name__ == "__main__":
    main(user_input=user_input, explain=is_explain_mode)