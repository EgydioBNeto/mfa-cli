#!/usr/bin/env python3

"""
Uninstall Script
"""

import os
import shutil
import re
from colors import GREEN, RESET

INSTALL_DIR = os.path.expanduser("~/mfa-cli")
CONFIG_FILES = [os.path.expanduser("~/.bashrc"), os.path.expanduser("~/.zshrc")]


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
