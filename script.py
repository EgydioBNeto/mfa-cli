#!/usr/bin/env python3
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
    try:
        with open(SECRET_FILE, "r") as file:
            content = file.read()
            if not content:
                return {} 
            secrets = json.loads(content)
        return secrets
    except FileNotFoundError:
        with open(SECRET_FILE, "w") as file:
            json.dump({}, file)
        return {}
    except (IOError, json.decoder.JSONDecodeError) as e:
        print(RED + f"Error handling secrets file: {str(e)}" + RESET)
        return {}

def save_secrets(secrets):
    mfa_cli_dir = os.path.join(os.path.expanduser("~"), "mfa-cli")
    os.makedirs(mfa_cli_dir, exist_ok=True)
    with open(SECRET_FILE, "w") as file:
        try:
            json.dump(secrets, file, indent=2)
        except IOError as e:
            print(RED + f"Error saving secrets: {str(e)}" + RESET)
    
def add_secret(name, secret):
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
    secrets = load_secrets()
    if name in secrets:
        del secrets[name]
        save_secrets(secrets)
        return print(GREEN + f"Secret {name} deleted successfully." + RESET)
    else:
        return print(RED + f"Secret {name} not found." + RESET)

def list_secrets():
    secrets = load_secrets()
    if secrets:
        print(YELLOW + "LIST OF STORED SECRETS:" + RESET)
        for count, (name, secret) in enumerate(secrets.items(), start=1):
            print(f"{count}. {name}")
    else:
        print(RED + "No secrets found." + RESET)

def update_secret(name, secret):
    load_secrets = load_secrets()
    if name in load_secrets:
        old_secret = load_secrets[name]
        load_secrets[name] = secret
        save_secrets(load_secrets)
        print(GREEN + f"Secret '{name}' updated successfully." + RESET)
        print(YELLOW + f"Old Secret: {old_secret}" + RESET)
        print(YELLOW + f"New Secret: {secret}"+ RESET)
    else:
        print(RED + f"Error: Secret with the name '{name}' not found." + RESET)

def export_secrets(file_path):
    file_path = os.path.join(os.getcwd(), file_path)
    secrets = load_secrets()
    try:
        with open(file_path, "w") as export_file:
            json.dump(secrets, export_file, indent=2)
        print(GREEN + f"Secrets exported successfully to '{file_path}'." + RESET)
    except IOError as e:
        print(RED + f"Error exporting secrets: {str(e)}" + RESET)

def help():
    print("MFA CLI - Help")
    print("Usage: mfa-cli <command> [options]")
    print("")
    print("Commands:")
    print("  add_secret <name> <secret>     Add a new secret")
    print("  delete_secret <name>           Delete a stored secret")
    print("  list_secrets                   List all stored secrets")
    print("  update_secret <name> <secret>  Update an existing secret")
    print("  generate_mfa <name>            Generate an MFA code")
    print("  export_secrets <file_path>     Export secrets to a file")
    print("  help                           Show this help message")
    print("")
    print("Examples:")
    print("")
    print("   Normal")
    print("     mfa_add my_secret_name my_secret_key")
    print("     mfa_delete my_secret_name")
    print("     mfa_list")
    print("     mfa_update my_secret_name new_secret_key")
    print("     mfa_generate my_secret_name")
    print("     mfa_export export_file.json")
    print("     mfa_help")
    print("")
    print("   Summarized")
    print("     mfa my_secret_name my_secret_key")
    print("     mfd my_secret_name")
    print("     mfl")
    print("     mfu my_secret_name new_secret_key")
    print("     mfg my_secret_name")
    print("     mfe export_file.json")
    print("     mfh")

def generate_mfa(name):
    secrets = load_secrets()
    if name in secrets:
        secret = secrets[name]
        try:
            # Add padding if necessary
            secret = secret.ljust((len(secret) + 7) // 8 * 8, '=')
            counter = int(time.time()) // 30  # Use time-based counter for TOTP
            secret_bytes = base64.b32decode(secret, casefold=True)
            message = struct.pack(">Q", counter)
            hmac_digest = hmac.new(secret_bytes, message, hashlib.sha1).digest()
            offset = hmac_digest[-1] & 0x0F
            truncated_hash = hmac_digest[offset:offset + 4]
            code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
            code = code % 1000000  # 6-digit code
            return print(GREEN + f"MFA {name}: ({code:06})" + RESET)
        except binascii.Error as e:
            return print(RED + f"Error generating MFA for {name}: {str(e)}" + RESET)
    else:
        return  print(RED + f"Secret for {name} not found." + RESET)

def main():
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
        pass
    elif args.command == "delete_secret":
        if len(args.args) == 1:
            name = args.args[0]
            delete_secret(name)
        else:
            print(RED + "Error: delete_secret command requires exactly one argument (name)." + RESET)
        pass
    elif args.command == "list_secrets":
        if len(args.args) == 0:
            list_secrets()
        else:
            print(RED + "Error: list_secrets command requires no arguments." + RESET)
        pass
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
        pass
    elif args.command == "help":
        if len(args.args) == 0:
            help()
        else:
            print(RED + "Error: help command requires no arguments." + RESET)

if __name__ == "__main__":
    main()
