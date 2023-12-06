#!/bin/bash

SCRIPT_NAME="script.py"
CONFIG_FILES=(~/.bashrc ~/.zshrc)

INSTALL_DIR="$HOME/mfa-cli"

mkdir -p "$INSTALL_DIR"

curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py  -o "$INSTALL_DIR/$SCRIPT_NAME"

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for config_file in "${CONFIG_FILES[@]}"; do
    echo "alias mfa export='$INSTALL_DIR/$SCRIPT_NAME export_secrets --export_file secrets.json'" >> "$config_file"
    echo "function mfa_add() {$INSTALL_DIR/$SCRIPT_NAME add_secret --name "$1" --secret "$2"} alias mfa add='mfa_add()'" >> "$config_file"
    echo "function mfa_delete() {$INSTALL_DIR/$SCRIPT_NAME delete_secret --name "$1"} alias mfa delete='mfa_delete()'" >> "$config_file"
    echo "function mfa_list() { $INSTALL_DIR/$SCRIPT_NAME list_secrets } alias mfa list='mfa_list()'" >> "$config_file"
    echo "function mfa_generate() { $INSTALL_DIR/$SCRIPT_NAME generate_mfa --name "$1"} alias mfa='mfa_generate()'" >> "$config_file"
    echo "function mfa_update() { $INSTALL_DIR/$SCRIPT_NAME update_secret --name "$1" --secret "$2"} alias mfa update='mfa_update()'" >> "$config_file"
    
done



echo "Script installed successfully, please restart your terminal!"
