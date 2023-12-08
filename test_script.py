#!/usr/bin/env python3

"""
mfa-cli test script
"""
import os
import json
from io import StringIO
import sys
from script import (add_secret, delete_secret, update_secret, list_secrets, generate_mfa, export_secrets, mfa_help)
from install import (install_mfa_cli, uninstall_mfa_cli)

def test_uninstall_mfa_cli():
    """
    Uninstall the 'mfa-cli' script.
    """

    uninstall_mfa_cli()

    script_path = os.path.expanduser("~/mfa-cli/script.py")
    assert not os.path.exists(script_path)

    zshrc_path = os.path.expanduser("~/.zshrc")
    assert not check_code_block_exists(zshrc_path)

    bashrc_path = os.path.expanduser("~/.bashrc")
    assert not check_code_block_exists(bashrc_path)

def test_install_mfa_cli():
    """
    Install the 'mfa-cli' script.
    """

    install_mfa_cli()

    script_path = os.path.expanduser("~/mfa-cli/script.py")
    assert os.path.exists(script_path)

    zshrc_path = os.path.expanduser("~/.zshrc")
    assert check_code_block_exists(zshrc_path)

    bashrc_path = os.path.expanduser("~/.bashrc")
    assert check_code_block_exists(bashrc_path)

def check_code_block_exists(file_path):
    """
    Check if a code block exists in a file.
    """
    start_marker = "# MFA CLI aliases start"
    end_marker = "# MFA CLI aliases end"

    try:
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read()
            return start_marker in content and end_marker in content
    except FileNotFoundError:
        return False


def check_secret_in_json(json_path, secret_name):
    """
    Check if a secret is in a JSON file.
    """
    try:
        with open(json_path, "r", encoding='utf-8') as file:
            secrets_data = json.load(file)
            return secret_name in secrets_data
    except FileNotFoundError:
        return False


def test_add_secret():
    """
    Test add_secret function
    """

    add_secret("secret", "secret_value")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    response = check_secret_in_json(secrets_path, "secret")
    assert response == True

def test_generate_mfa(capsys):
    """
    Test generate_mfa function
    """
    name = "generate"
    add_secret(name, "H5U5Q3VFPMZAMVE3")
    generate_mfa(name)
    captured = capsys.readouterr()
    assert f"Error generating MFA for {name}" not in captured.out
    assert f"Secret for {name} not found." not in captured.out

def test_update_secret():
    """
    Test update_secret function
    """
    update_secret("secret", "123")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    with open(secrets_path, "r", encoding='utf-8') as file:
        secrets_data = json.load(file)
        print("secrets_data:", secrets_data)


    assert secrets_data.get("secret") == "123"

def test_list_secrets():
    """
    Test list_secrets function
    """
    captured_output = StringIO()
    sys.stdout = captured_output
    list_secrets()
    result = captured_output.getvalue()
    assert "123" in result, f"String '123' not found in the response: {result}"

def test_mfa_help():
    """
    Test mfa_help function
    """
    mfa_help()
    assert True

def test_export_secrets():
    """
    Test export_secrets function
    """
    export_secrets("test.json")
    assert os.path.exists("test.json")
    os.remove("test.json")

def test_delete_secret():
    """
    Test delete_secret function
    """
    delete_secret("secret")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    response = check_secret_in_json(secrets_path, "secret")
    assert response == False
