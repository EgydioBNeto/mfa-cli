#!/bin/bash

SCRIPT_NAME="script.py"
CONFIG_FILES=(~/.bashrc ~/.zshrc)

INSTALL_DIR="$HOME/mfa-cli"

mkdir -p "$INSTALL_DIR"

curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py  -o "$INSTALL_DIR/$SCRIPT_NAME"

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

for config_file in "${CONFIG_FILES[@]}"; do

echo "
# MFA CLI aliases start
alias 'mfa export'='$INSTALL_DIR/$SCRIPT_NAME export_secrets --export_file secrets.json'
alias 'mfa add'='$INSTALL_DIR/$SCRIPT_NAME add_secret'
alias 'mfa list'='$INSTALL_DIR/$SCRIPT_NAME list_secrets'
alias 'mfa generate'='$INSTALL_DIR/$SCRIPT_NAME generate_mfa'
alias 'mfa update'='$INSTALL_DIR/$SCRIPT_NAME update_secret'
alias 'mfa delete'='$INSTALL_DIR/$SCRIPT_NAME delete_secret'
alias 'mfa help'='$INSTALL_DIR/$SCRIPT_NAME help'
# MFA CLI aliases end
" >> "$config_file"
done

echo "Script installed successfully, please restart your terminal!"
