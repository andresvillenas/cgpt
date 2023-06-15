# cgpt (command-GPT) 🖥️⚡

cgpt is your friendly command line helper! Powered by OpenAI, cgpt simplifies your command line experience by transforming everyday language into useful command line statements. It supports Windows, Linux, and MacOS environments. Whether you're a beginner learning the ropes or an expert who occasionally forgets syntax, cgpt is here to help! 🚀

## Features 🎁

- 🤖 AI-Powered: Leverages OpenAI's GPT-3 to understand and process commands.
- 🌐 Cross-Platform: Works on Windows, Linux and MacOS.
- 🛠️ Command Line Interface: Easy to use and fits right into your workflow.
- 📖 Explain Mode: Provides explanations for generated commands.
- 🛡️ Safe: Always asks for confirmation before executing commands, with additional warnings for potentially dangerous operations.

## Demo
https://github.com/andresvillenas/cgpt/assets/4082342/b3cd1f8f-f72c-48f4-8939-40d4a0899f0a

## Installation 📦

### Windows
1. Download the latest cgpt-installer.exe from the [releases](https://github.com/andresvillenas/cgpt/releases) page.
2. Run the installer and follow the prompts to install cgpt.
   - You will be asked to enter your OpenAI API key during the installation process.
   - The installer will add the cgpt installation directory to your system's PATH, allowing you to run cgpt from the command line.
3. Once the installation process is complete, you can verify that cgpt was installed correctly by opening a new command prompt window and running cgpt.
   
Please note that updating your cgpt installation to a new version is as simple as running the new installer — there's no need to manually uninstall the old version first.

## Usage 🚦

Once installed, you can start using CGPT by entering commands like so:

```shell
cgpt "create a new directory called test" # the -i parameter is not required anymore since v0.2.0
```
If you want an explanation of the generated command, use the -e or --explain flag:
```shell
cgpt "create a new directory called test" -e
```
If the command can potentially affect your system, CGPT will warn you and ask for confirmation before proceeding.

## Development 🛠️
Comming soon

## Contributing 🤝
We welcome contributions from everyone. Please read our [contributing guide](documentation/CONTRIBUTING.md) to get started.

## License


## Acknowledgements 🙏
CGPT uses the following open source software:

- OpenAI's GPT-3: For understanding and processing commands.
- Python: For the core application.

## Support 💖
If you like CGPT, consider starring the repository and sharing it with your friends!

Enjoy using CGPT! 🎉
