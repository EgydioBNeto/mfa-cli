from script import (add_secret)

def test_add_secret(capfd):
    # Add a secret and check if it was added successfully
    add_secret("new_secret", "secret_value")
    captured = capfd.readouterr()

    assert"Error: Secret with the name 'new_secret' already exists" in captured.out or "Secret added successfully." in captured.out
