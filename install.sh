#!/bin/bash

SCRIPT_NAME="script.py"
CONFIG_FILES=(~/.bashrc ~/.zshrc)

INSTALL_DIR="$HOME/mfa-cli"

mkdir -p "$INSTALL_DIR"

curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py  -o "$INSTALL_DIR/$SCRIPT_NAME"

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for config_file in "${CONFIG_FILES[@]}"; do

echo "
alias mfa_export='~/mfa-cli/script.py export_secrets --export_file secrets.json'
function mfa_add() {
    ~/mfa-cli/script.py add_secret --name "$1" --secret "$2"
}
alias mfa_add='mfa_add()'
function mfa_delete() {
    ~/mfa-cli/script.py delete_secret --name "$1"
}
alias mfa_delete='mfa_delete()'
function mfa_list() {
    ~/mfa-cli/script.py list_secrets
}
alias mfa_list='mfa_list()'
function mfa_generate() {
    ~/mfa-cli/script.py generate_mfa --name "$1"
}
alias mfa_generate='mfa_generate()'
function mfa_update() {
    ~/mfa-cli/script.py update_secret --name "$1" --secret "$2"
}
alias mfa_update='mfa_update()'
alias mfa_help='~/mfa-cli/script.py help'
" >> "$config_file"
    
done



echo "Script installed successfully, please restart your terminal!"
