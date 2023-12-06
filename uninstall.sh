#!/bin/bash

INSTALL_DIR="$HOME/mfa-cli"
rm -rf "$INSTALL_DIR"

CONFIG_FILES=(~/.bashrc ~/.zshrc)

for config_file in "${CONFIG_FILES[@]}"; do
    sed -i '/# MFA CLI aliases start/,/# MFA CLI aliases end/d' "$config_file"
done

echo -e "\033[92m Environment clenup complete.\033[0m"
