#!/usr/bin/env python3

"""
mfa-cli Script
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

MAX_SECRET_LENGTH = 256
SECRET_FILE = os.path.join(os.path.expanduser("~"), "mfa-cli", "secrets.json")

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def load_secrets():
    """
    Load secrets.
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
    """
    secrets = load_secrets()
    if name in secrets:
        secret = secrets[name]
        try:
            # Add padding if necessary
            secret = secret.ljust((len(secret) + 7) // 8 * 8, '=')
            counter = int(time.time()) // 30 
            secret_bytes = base64.b32decode(secret, casefold=True)
            message = struct.pack(">Q", counter)
            hmac_digest = hmac.new(secret_bytes, message, hashlib.sha1).digest()
            offset = hmac_digest[-1] & 0x0F
            truncated_hash = hmac_digest[offset:offset + 4]
            code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
            code = code % 1000000
            print (GREEN + f"MFA code for {name}: {code:06}" + RESET)
            return code
        except binascii.Error as export_error:
            return print(RED + f"Error generating MFA for {name}: {str(export_error)}" + RESET)
    else:
        return print(RED + f"Secret for {name} not found." + RESET)

def main():
    """
    Parse command-line arguments and execute the corresponding command.
    """
    parser = argparse.ArgumentParser(description="CLI to store secrets and generate MFA codes.")
    parser.add_argument("command", choices=["add_secret", "generate_mfa", "delete_secret", "list_secrets", "update_secret", "export_secrets", "help"], help="Command to execute.")
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
    elif args.command == "help":
        if len(args.args) == 0:
            help()
        else:
            print(RED + "Error: help command requires no arguments." + RESET)

if __name__ == "__main__":
    main()
