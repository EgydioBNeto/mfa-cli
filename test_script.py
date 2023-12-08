import os
import json
from script import (add_secret, delete_secret, update_secret, list_secrets, generate_mfa, export_secrets, mfa_help)
from install import (install_mfa_cli, uninstall_mfa_cli)
from io import StringIO
import sys

def test_uninstall_mfa_cli():

    uninstall_mfa_cli()

    script_path = os.path.expanduser("~/mfa-cli/script.py")
    assert not os.path.exists(script_path)

    zshrc_path = os.path.expanduser("~/.zshrc")
    assert not check_code_block_exists(zshrc_path)

    bashrc_path = os.path.expanduser("~/.bashrc")
    assert not check_code_block_exists(bashrc_path)

def test_install_mfa_cli():

    install_mfa_cli()

    script_path = os.path.expanduser("~/mfa-cli/script.py")
    assert os.path.exists(script_path)

    zshrc_path = os.path.expanduser("~/.zshrc")
    assert check_code_block_exists(zshrc_path)

    bashrc_path = os.path.expanduser("~/.bashrc")
    assert check_code_block_exists(bashrc_path)

def check_code_block_exists(file_path):
    start_marker = "# MFA CLI aliases start"
    end_marker = "# MFA CLI aliases end"

    try:
        with open(file_path, "r") as file:
            content = file.read()
            return start_marker in content and end_marker in content
    except FileNotFoundError:
        return False


def check_secret_in_json(json_path, secret_name):
    try:
        with open(json_path, "r") as file:
            secrets_data = json.load(file)
            return True if secret_name in secrets_data else False
    except FileNotFoundError:
        return False 
    
def test_add_secret():
    
    add_secret("secret", "secret_value")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    response = check_secret_in_json(secrets_path, "secret")
    assert response == True

def test_generate_mfa(capsys):
    name = "generate"
    add_secret(name, "H5U5Q3VFPMZAMVE3")
    generate_mfa(name)
    captured = capsys.readouterr()
    assert f"Error generating MFA for {name}" not in captured.out
    assert f"Secret for {name} not found." not in captured.out

def test_update_secret():

    update_secret("secret", "123")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    with open(secrets_path, "r") as file:
        secrets_data = json.load(file)
        print("secrets_data:", secrets_data)


    assert secrets_data.get("secret") == "123"

def test_list_secrets():

    captured_output = StringIO()
    sys.stdout = captured_output
    list_secrets()
    result = captured_output.getvalue()
    assert "123" in result, f"String '123' not found in the response: {result}"

def test_delete_secret():

    delete_secret("secret")
    secrets_path = os.path.expanduser("~/mfa-cli/secrets.json")
    response = check_secret_in_json(secrets_path, "secret")
    assert response == False

