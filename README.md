# Multi-Factor Authentication Command Line Interface

<div align="center">
<img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/714533aa-22a2-4127-8d40-363e59a573fa" width="300px"/>
</div>

## Languages

[English](https://github.com/EgydioBNeto/mfa-cli/blob/main/README.md), [Portuguese-BR](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/pt-br/README.md), [Spanish](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/es/README.md), [German](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/de/README.md), [French](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/fr/README.md), [Russian](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/ru/README.md), [Chinese](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/zh/README.md), [Japanese](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/ja/README.md), [Hindi](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/hi/README.md), [Arabic](https://github.com/EgydioBNeto/mfa-cli/blob/main/languages/ar/README.md)

## Description

This is a simple Command Line Interface (CLI) tool written in Python for managing secrets and generating Multi-Factor Authentication (MFA) codes. The script allows users to add, delete, update, list, and export secrets, as well as generate MFA codes.

## Overview

<div align="center">
<img src="https://github.com/EgydioBNeto/mfa-cli/assets/84047984/4fe8c766-8e76-4183-a80c-9ac143cbc18f" width="1000px"/>
</div>

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

- **Python3**

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
