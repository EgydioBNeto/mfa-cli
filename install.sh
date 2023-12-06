#!/bin/bash

SCRIPT_NAME="script.py"
CONFIG_FILES=(~/.bashrc ~/.zshrc)
MFA_CLI_DIR=~/mfa-cli
INSTALL_DIR="$HOME/mfa-cli"




if [ -d "$MFA_CLI_DIR" ]; then
    echo -e "mfa-cli' already exists. Proceeding with clenup."
    bash -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.sh)"
    mkdir -p "$INSTALL_DIR"
else
    echo -e "Directory 'mfa-cli' does not exist. Proceeding with installation."
    mkdir -p "$INSTALL_DIR"
fi

curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py  -o "$INSTALL_DIR/$SCRIPT_NAME"

chmod +x "$INSTALL_DIR/$SCRIPT_NAME"

for config_file in "${CONFIG_FILES[@]}"; do

echo "
# MFA CLI aliases start
alias mfa_export='$INSTALL_DIR/$SCRIPT_NAME export_secrets'
alias mfa_add='$INSTALL_DIR/$SCRIPT_NAME add_secret'
alias mfa_list='$INSTALL_DIR/$SCRIPT_NAME list_secrets'
alias mfa_generate='$INSTALL_DIR/$SCRIPT_NAME generate_mfa'
alias mfa_update='$INSTALL_DIR/$SCRIPT_NAME update_secret'
alias mfa_delete='$INSTALL_DIR/$SCRIPT_NAME delete_secret'
alias mfa_help='$INSTALL_DIR/$SCRIPT_NAME help'
alias mfe='$INSTALL_DIR/$SCRIPT_NAME export_secrets'
alias mfa='$INSTALL_DIR/$SCRIPT_NAME add_secret'
alias mfl='$INSTALL_DIR/$SCRIPT_NAME list_secrets'
alias mfg='$INSTALL_DIR/$SCRIPT_NAME generate_mfa'
alias mfu='$INSTALL_DIR/$SCRIPT_NAME update_secret'
alias mfd='$INSTALL_DIR/$SCRIPT_NAME delete_secret'
alias mfh='$INSTALL_DIR/$SCRIPT_NAME help'
# MFA CLI aliases end
" >> "$config_file"

done

echo -e "\033[92mmfa-cli installed successfully, please restart your terminal!\033[0m"
