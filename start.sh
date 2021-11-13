#!/bin/bash
echo " "
echo "Starting the script..."
echo "1 - Installing dependencies"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install p7zip
brew install python
brew install python3
brew install pip
echo "2 - Cleaning"
brew cleanup
echo "3 - Running the patcher"
python3 installer.py
