#!/usr/bin/env python3

"""
Uninstall Script
"""

import os
import shutil
import re

INSTALL_DIR = os.path.expanduser("~/mfa-cli")
CONFIG_FILES = [os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.zshrc")]

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

if os.path.exists(INSTALL_DIR):
    shutil.rmtree(INSTALL_DIR)

for config_file in CONFIG_FILES:
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        with open(config_file, 'w', encoding='utf-8') as f:
            for line in lines:
                if not re.search(r'# MFA CLI aliases (start|end)', line):
                    f.write(line)

print(GREEN + "Environment cleanup complete." + RESET)
