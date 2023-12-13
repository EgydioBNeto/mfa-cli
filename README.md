# MFA CLI

div align="center"
img src="![MFA-CLI-removebg-preview](https://github.com/EgydioBNeto/mfa-cli/assets/84047984/309bae4c-8110-45b1-8999-33ab3d9f9136)" width="0px" /
/div

## Description

This is a simple Command Line Interface (CLI) tool written in Python for managing secrets and generating Multi-Factor Authentication (MFA) codes. The script allows users to add, delete, update, list, and export secrets, as well as generate MFA codes.

## Features

### Commands

- **mfa_add** &lt;name&gt; &lt;secret&gt;: Add a new secret.
- **mfa_delete** &lt;name&gt; Delete a stored secret.
- **mfa_list** List all stored secrets.
- **mfa_update** &lt;name&gt; &lt;secret&gt;: Update an existing secret.
- **mfa_generate** &lt;name&gt;: Generate an MFA code.
- **mfa_export** &lt;file_path&gt;: Export secrets to a file.
- **mfa_help** Show this help message.

### Summarized Commands

- **mfa** &lt;name&gt; &lt;secret&gt;: Add a new secret.
- **mfd** &lt;name&gt; Delete a stored secret.
- **mfl** List all stored secrets.
- **mfu** &lt;name&gt; &lt;secret&gt;: Update an existing secret.
- **mfg** &lt;name&gt;: Generate an MFA code.
- **mfe** &lt;file_path&gt;: Export secrets to a file.
- **mfh** Show this help message.

## Requirements

Python 3

## Installation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/install.py)"
```

## Uninstallation

```bash
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/EgydioBNeto/mfa-cli/main/uninstall.py)"
```

## Author

[EgydioBNeto](https://github.com/EgydioBNeto)

## License

This project is licensed under the [MIT License](https://github.com/EgydioBNeto/mfa-cli/blob/main/LICENSE).

