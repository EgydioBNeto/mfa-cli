# MFA CLI

## Description

This is a simple Command Line Interface (CLI) tool written in Python for managing secrets and generating Multi-Factor Authentication (MFA) codes. The script allows users to add, delete, update, list, and export secrets, as well as generate MFA codes.

## Installation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Features

### Commands

- **mfa_add** <name> <secret>: Add a new secret.
- **mfa_delete** <name>: Delete a stored secret.
- **mfa_list** List all stored secrets.
- **mfa_update** <name> <secret>: Update an existing secret.
- **mfa_generate** <name>: Generate an MFA code.
- **mfa_export** <file_path>: Export secrets to a file.
- **mfa_help** Show this help message.

### Summarized Commands

- **mfa** <name> <secret>: Add a new secret.
- **mfd** <name>: Delete a stored secret.
- **mfl** List all stored secrets.
- **mfu** <name> <secret>: Update an existing secret.
- **mfg** <name>: Generate an MFA code.
- **mfe** <file_path>: Export secrets to a file.
- **mfh** Show this help message.

## Uninstallation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Requirements

Python 3

## Author

[EgydioBNeto](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE)

## License

This project is licensed under the [MIT License](URL_do_Link).

