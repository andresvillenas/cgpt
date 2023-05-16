# settings.py
import configparser
import os
import sys


class Config:

    class OpenAI:
        def __init__(self, config):
            self.api_key = config['openai']['api_key']

    class Prompts:
        def __init__(self, config):
            self.prompts_folder = config['prompts']['prompts_folder']
            self.default_prompt_file = config['prompts']['default_prompt_file']
            self.prompt_file_extension = config['prompts']['prompt_file_extension']

    def __init__(self):
        # Initialize configparser
        self.config = configparser.ConfigParser()

        if getattr(sys, 'frozen', False):
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.dirname(os.path.dirname(__file__))

        config_path = os.path.join(application_path, 'config.ini')

        self.config.read(config_path)

        self.openai = self.OpenAI(self.config)

        self.prompts = self.Prompts(self.config)
