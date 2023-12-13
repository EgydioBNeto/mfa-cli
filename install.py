#!/usr/bin/env python3

"""
Install Script

This script is used to install the 'mfa-cli' tool. It downloads the necessary files from a GitHub repository,
sets up aliases in the user's configuration files, and provides a convenient way to manage multi-factor authentication secrets.

The script first checks if 'mfa-cli' is already installed and, if so, it uninstalls it before proceeding with the installation.

Usage:
    python install.py

Note: After installation, it is recommended to restart the terminal for the aliases to take effect.
"""

import sys
import os
import subprocess

SCRIPT_NAME = "script.py"
CONFIG_FILES = [os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.zshrc")]
INSTALL_DIR = os.path.expanduser("~/mfa-cli")
INSTALL_URL = "https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/script.py"
UNINSTALL_URL = "https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def uninstall_mfa_cli():
    """
    Uninstall the 'mfa-cli' script.

    This function downloads the uninstall script from the GitHub repository and runs it.
    """
    print("Uninstalling existing 'mfa-cli'...")

    try:
        subprocess.run(["curl", "-fsSL", UNINSTALL_URL, "-o", f"{INSTALL_DIR}/uninstall.py"], check=True)
    except subprocess.CalledProcessError:
        print(f"Cannot download uninstall script from '{UNINSTALL_URL}'.")
        print("Please uninstall manually.")
        return

    os.chmod(f"{INSTALL_DIR}/uninstall.py", 0o755)

    try:
        subprocess.run([f"{INSTALL_DIR}/uninstall.py"], check=True)
    except subprocess.CalledProcessError:
        print("Uninstall script failed.")
        print("Please uninstall manually.")
        return
    
def install_mfa_cli():
    """
    Install the 'mfa-cli' script.

    This function downloads the script from the GitHub repository, sets up aliases in the user's configuration files,
    """
    print("Installing 'mfa-cli'...")
    os.makedirs(INSTALL_DIR, exist_ok=True)
    subprocess.run(["curl", "-fsSL", INSTALL_URL, "-o", f"{INSTALL_DIR}/{SCRIPT_NAME}"], check=True)
    os.chmod(f"{INSTALL_DIR}/{SCRIPT_NAME}", 0o755)
    for config_file in CONFIG_FILES:
        with open(config_file, "a", encoding="utf-8") as alias_file:
            alias_file.write(f"""
# MFA CLI aliases start
alias mfa_export='{INSTALL_DIR}/{SCRIPT_NAME} export_secrets'
alias mfa_add='{INSTALL_DIR}/{SCRIPT_NAME} add_secret'
alias mfa_list='{INSTALL_DIR}/{SCRIPT_NAME} list_secrets'
alias mfa_generate='{INSTALL_DIR}/{SCRIPT_NAME} generate_mfa'
alias mfa_update='{INSTALL_DIR}/{SCRIPT_NAME} update_secret'
alias mfa_delete='{INSTALL_DIR}/{SCRIPT_NAME} delete_secret'
alias mfa_help='{INSTALL_DIR}/{SCRIPT_NAME} help'
alias mfe='{INSTALL_DIR}/{SCRIPT_NAME} export_secrets'
alias mfa='{INSTALL_DIR}/{SCRIPT_NAME} add_secret'
alias mfl='{INSTALL_DIR}/{SCRIPT_NAME} list_secrets'
alias mfg='{INSTALL_DIR}/{SCRIPT_NAME} generate_mfa'
alias mfu='{INSTALL_DIR}/{SCRIPT_NAME} update_secret'
alias mfd='{INSTALL_DIR}/{SCRIPT_NAME} delete_secret'
alias mfh='{INSTALL_DIR}/{SCRIPT_NAME} help'
# MFA CLI aliases end
""")
    print(GREEN + "mfa-cli installed successfully, please restart your terminal!" + RESET)
    
def main():
    """
    Main function.

    This function checks if 'mfa-cli' is already installed and, if so, it uninstalls it before proceeding with the installation.
    """
    if os.path.exists(INSTALL_DIR):
        uninstall_mfa_cli()

    install_mfa_cli()

if __name__ == "__main__":
    try:
        main()
    except Exception as exception_error:
        print(exception_error)
        sys.exit(1)
