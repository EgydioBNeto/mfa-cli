#!/usr/bin/env python3

"""
Install Script
"""

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


if os.path.exists(INSTALL_DIR):
    print("'mfa-cli' already exists. Proceeding with cleanup.")

    # Add uninstallation logic here
    subprocess.run(["curl", "-fsSL", UNINSTALL_URL, "-o", f"{INSTALL_DIR}/uninstall.py"], check=True)
    os.chmod(f"{INSTALL_DIR}/uninstall.py", 0o755)
    subprocess.run([f"{INSTALL_DIR}/uninstall.py"], check=True)

else:
    print("Directory 'mfa-cli' does not exist. Proceeding with installation.")
    os.makedirs(INSTALL_DIR, exist_ok=True)


    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)

    subprocess.run(["curl", "-fsSL", INSTALL_URL, "-o", f"{INSTALL_DIR}/{SCRIPT_NAME}"], check=True)
    os.chmod(f"{INSTALL_DIR}/{SCRIPT_NAME}", 0o755)

    for config_file in CONFIG_FILES:
        with open(config_file, "a", encoding="utf-8") as f:
            f.write(f"""
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
