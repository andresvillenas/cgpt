# Script to build the cgpt installer for windows

# Activates the virtual environment
..\..\cgpt\env\Scripts\activate.ps1

# Removes the build and dist folders
Remove-Item build -r
Remove-Item dist -r 

# Builds the cgpt executable
pyinstaller --onefile --add-data "..\..\cgpt\prompts;prompts" --distpath ".\dist\" "..\..\cgpt\cgpt.py"

# Copies the config file to the dist folder
Copy-Item ..\..\cgpt\config.ini .\dist\config.ini

# Builds the installer
& 'C:\Program Files (x86)\Inno Setup 6\ISCC.exe' cgpt-installer.iss    
