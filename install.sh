#!/bin/bash

# Define the alias and script name
ALIAS_NAME="MFA"
SCRIPT_NAME="script.py"

# Installation directory
INSTALL_DIR="$HOME/mfa-cli"

# Create the installation directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py  -o "$INSTALL_DIR/$SCRIPT_NAME"

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

# Full path to the directory where the installation script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add the alias to the bash configuration file
echo "alias $ALIAS_NAME='$INSTALL_DIR/$SCRIPT_NAME'" >> ~/.bashrc

# Add the alias to the zsh configuration file
echo "alias $ALIAS_NAME='$INSTALL_DIR/$SCRIPT_NAME'" >> ~/.zshrc


echo "Script installed successfully, please restart your terminal!"
