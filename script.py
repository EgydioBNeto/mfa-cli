"""
mfa-cli Script

This script provides a command-line interface (CLI) for storing secrets and generating MFA (Multi-Factor Authentication) codes.
The script allows users to add, delete, update, and list secrets, as well as generate MFA codes for specific secrets.
Secrets are stored in a JSON file located at ~/.mfa-cli/secrets.json.

Usage:
    python script.py <command> [options]

Commands:
    add_secret <name> <secret>     Add a new secret
    delete_secret <name>           Delete a stored secret
    list_secrets                   List all stored secrets
    update_secret <name> <secret>  Update an existing secret
    generate_mfa <name>            Generate an MFA code
    export_secrets <file_path>     Export secrets to a file
    mfa_help                           Show this help message

Examples:
    python script.py add_secret my_secret_name my_secret_key
    python script.py delete_secret my_secret_name
    python script.py list_secrets
    python script.py update_secret my_secret_name new_secret_key
    python script.py generate_mfa my_secret_name
    python script.py export_secrets export_file.json
    python script.py help
"""

import argparse
import hashlib
import hmac
import base64
import json
import struct
import time
import binascii
import os
import sys

MAX_SECRET_LENGTH = 256
SECRET_FILE = os.path.join(os.path.expanduser("~"), "mfa-cli", "secrets.json")
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def load_secrets():
    """
    Load secrets from a file.

    This function reads the contents of a secret file, parses it as JSON,
    and returns the secrets as a dictionary. If the file does not exist,
    it creates an empty file and returns an empty dictionary.

    Returns:
        dict: A dictionary containing the loaded secrets.

    """
    try:
        with open(SECRET_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            if not content:
                return {}
            secrets = json.loads(content)
        return secrets
    except FileNotFoundError:
        with open(SECRET_FILE, "w", encoding="utf-8") as file:
            json.dump({}, file)
        return {}
    except (IOError, json.decoder.JSONDecodeError) as export_error:
        print(RED + f"Error handling secrets file: {str(export_error)}" + RESET)
        return {}

def save_secrets(secrets):
    """
    Save secrets.

    This function saves the provided secrets to a file named SECRET_FILE.
    The secrets are serialized as JSON and written to the file.

    """
    mfa_cli_dir = os.path.join(os.path.expanduser("~"), "mfa-cli")
    os.makedirs(mfa_cli_dir, exist_ok=True)
    with open(SECRET_FILE, "w", encoding="utf-8") as file:
        try:
            json.dump(secrets, file, indent=2)
        except IOError as export_error:
            print(RED + f"Error saving secrets: {str(export_error)}" + RESET)

def add_secret(name, secret):
    """
    Add a secret.

    This function adds a secret to the secrets file. If the secret already exists,
    it prints an error message and does not add the secret. If the secret does not
    exist, it adds the secret to the secrets file.
        
    """
    if name and secret is not None:
        if name not in load_secrets():
            if 1 <= len(secret) <= MAX_SECRET_LENGTH:
                secrets = load_secrets()
                secrets[name] = secret
                save_secrets(secrets)
                print(GREEN + "Secret added successfully." + RESET)
            else:
                print(RED + f"Error: Secret length should be between 1 and {MAX_SECRET_LENGTH} characters." + RESET)
        else:
            print(RED + f"Error: Secret with the name '{name}' already exists." + RESET)
    else:
        print(RED + "Error: Name and secret value cannot be null." + RESET)

def delete_secret(name):
    """
    Delete a secret.

    This function deletes a secret from the secrets file. If the secret does not exist,
    it prints an error message and does not delete the secret. If the secret exists,
    it deletes the secret from the secrets file.

    """
    secrets = load_secrets()
    if name in secrets:
        del secrets[name]
        save_secrets(secrets)
        print(GREEN + f"Secret {name} deleted successfully." + RESET)
    else:
        print(RED + f"Secret {name} not found." + RESET)

def list_secrets():
    """
    List all stored secrets.

    This function lists all the secrets stored in the secrets file.
    """
    secrets = load_secrets()
    if secrets:
        print(YELLOW + "LIST OF STORED SECRETS:" + RESET)
        for count, (name) in enumerate(secrets.items(), start=1):
            print(f"{count}. {name}")
    else:
        print(RED + "No secrets found." + RESET)

def update_secret(name, secret):
    """
    Update an existing secret.

    This function updates an existing secret in the secrets file. If the secret does not exist, it prints an error message.
    """
    try:
        secrets = load_secrets()
        old_secret = secrets.get(name)

        if old_secret is not None:
            secrets[name] = secret
            save_secrets(secrets)
            print(GREEN + f"Secret '{name}' updated successfully." + RESET)
            print(YELLOW + f"Old Secret: {old_secret}" + RESET)
            print(YELLOW + f"New Secret: {secret}" + RESET)
        else:
            print(RED + f"Error: Secret with the name '{name}' not found." + RESET)
    except FileNotFoundError:
        print(RED + "Error: Secrets file not found." + RESET)
    except IOError as export_error1:
        print(RED + f"Error accessing secrets file: {str(export_error1)}" + RESET)
    except json.decoder.JSONDecodeError as export_error2:
        print(RED + f"Error decoding JSON in secrets file: {str(export_error2)}" + RESET)


def export_secrets(file_path):
    """
    Export secrets to a file.

    This function exports the secrets to a file. If the export fails, it prints an error message.
    """
    file_path = os.path.join(os.getcwd(), file_path)
    secrets = load_secrets()
    try:
        with open(file_path, "w", encoding="utf-8") as export_file:
            json.dump(secrets, export_file, indent=2)
        print(GREEN + f"Secrets exported successfully to '{file_path}'." + RESET)
    except IOError as export_error:
        print(RED + f"Error exporting secrets: {str(export_error)}" + RESET)

def mfa_help():
    """
    Show help message.

    This function shows a help message with the available commands.
    """
    print ("""
        MFA CLI - Help
            Usage: mfa-cli <command> [options]

            Commands:
            add_secret <name> <secret>     Add a new secret
            delete_secret <name>           Delete a stored secret
            list_secrets                   List all stored secrets
            update_secret <name> <secret>  Update an existing secret
            generate_mfa <name>            Generate an MFA code
            export_secrets <file_path>     Export secrets to a file
            help                           Show this help message

            Examples:

            Normal
                mfa_add my_secret_name my_secret_key
                mfa_delete my_secret_name
                mfa_list
                mfa_update my_secret_name new_secret_key
                mfa_generate my_secret_name
                mfa_export export_file.json
                mfa_help

            Summarized
                mfa my_secret_name my_secret_key
                mfd my_secret_name
                mfl
                mfu my_secret_name new_secret_key
                mfg my_secret_name
                mfe export_file.json
                mfh
        
    """)
    return True

def generate_mfa(name):
    """
    Generate MFA code.

    This function generates an MFA code for the specified secret. If the secret does not exist, it prints an error message.
    """
    # Load secrets from the secrets file
    secrets = load_secrets()

    # Check if the named secret exists
    if name in secrets:
        # Get the secret and pad it to a multiple of 8 bytes
        secret = secrets[name]
        try:
            secret = secret.ljust((len(secret) + 7) // 8 * 8, '=')
            counter = int(time.time()) // 30 

            # Decode the secret from base32
            secret_bytes = base64.b32decode(secret, casefold=True)

            # Calculate the hash for the current time
            message = struct.pack(">Q", counter)
            # Calculate the HMAC-SHA1 of the hash
            hmac_digest = hmac.new(secret_bytes, message, hashlib.sha1).digest()
            # Get the offset
            offset = hmac_digest[-1] & 0x0F
            # Get the 4 bytes at the offset
            truncated_hash = hmac_digest[offset:offset + 4]
            # Unpack the 4 bytes as a 32-bit big-endian integer
            code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
            # Get the code as a 6-digit integer
            code = code % 1000000
            # Print the code
            print (GREEN + f"{code:06}" + RESET)
            return code
        except binascii.Error as export_error:
            return print(RED + f"Error generating MFA for {name}: {str(export_error)}" + RESET)
    else:
        return print(RED + f"Secret for {name} not found." + RESET)

def main():
    """
    Main function.

    This function parses the command-line arguments and executes the corresponding command.
    """
    parser = argparse.ArgumentParser(description="CLI to store secrets and generate MFA codes.")
    parser.add_argument("command", choices=["add_secret", "generate_mfa", "delete_secret", "list_secrets", "update_secret", "export_secrets", "mfa_help"], help="Command to execute.")
    parser.add_argument("args", nargs=argparse.REMAINDER, help="Arguments for the command.")

    args = parser.parse_args()

    if args.command == "add_secret":
        if len(args.args) == 2:
            name, secret = args.args
            add_secret(name, secret)
        else:
            print(RED + "Error: add_secret command requires exactly two arguments (name and secret)." + RESET)
    elif args.command == "generate_mfa":
        if len(args.args) == 1:
            name = args.args[0]
            generate_mfa(name)
        else:
            print(RED + "Error: generate_mfa command requires exactly one argument (name)." + RESET)
    elif args.command == "delete_secret":
        if len(args.args) == 1:
            name = args.args[0]
            delete_secret(name)
        else:
            print(RED + "Error: delete_secret command requires exactly one argument (name)." + RESET)
    elif args.command == "list_secrets":
        if len(args.args) == 0:
            list_secrets()
        else:
            print(RED + "Error: list_secrets command requires no arguments." + RESET)
    elif args.command == "update_secret":
        if len(args.args) == 2:
            name, secret = args.args
            update_secret(name, secret)
        else:
            print(RED + "Error: update_secret command requires exactly two arguments (name and new secret)." + RESET)
    elif args.command == "export_secrets":
        if len(args.args) == 1:
            file_path = args.args[0]
            export_secrets(file_path)
        else:
            print(RED + "Error: export_secrets command requires exactly one argument (file path)." + RESET)
    elif args.command == "mfa_help":
        if len(args.args) == 0:
            mfa_help()
        else:
            print(RED + "Error: help command requires no arguments." + RESET)

if __name__ == "__main__":
    try:
        main()
    except Exception as exception_error:
        print(exception_error)
        sys.exit(1)
