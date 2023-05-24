import os
import sys
from jinja2 import Template


class PromptService:
    """
    Service to load the prompt from the default prompt file and replace the placeholders with the appropriate values
    """

    def __init__(self, prompts_folder, default_prompt_file):
        self.prompts_folder = prompts_folder
        self.default_prompt_file = default_prompt_file

    def load_prompt(self, user_input, include_explanation):
        """
        Loads the prompt from the default prompt file and replaces the placeholders with the appropriate values

        :param user_input: The user input command
        :param include_explanation: Whether to include the explanation in the prompt
        :return: The prompt
        """

        os_name = 'Windows' if os.name == 'nt' else 'Linux'

        # Get the path to the prompts directory
        if getattr(sys, 'frozen', False):
            # If running from a standalone executable, use the _MEIPASS directory
            prompts_folder = os.path.join(sys._MEIPASS, self.prompts_folder)
        else:
            # If running from a development environment, use the prompts directory in the current directory
            prompts_folder = os.path.join(os.path.dirname(__file__), self.prompts_folder)

        # Construct the full path to the prompt file
        prompt_path = os.path.join(prompts_folder, self.default_prompt_file)

        # Read the prompt from the file
        with open(prompt_path, "r") as f:
            prompt_template = f.read()

        template = Template(prompt_template)

        prompt = template.render(os_name=os_name, user_input=user_input, include_explanation=include_explanation)

        return prompt