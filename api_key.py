# Script for Generating API Keys

import uuid


def generate_api_key():
    return str(uuid.uuid4())


def save_api_key(api_key, filename="api_keys.txt"):
    with open(filename, "a") as file:
        file.write(api_key + "\n")


if __name__ == "__main__":
    new_api_key = generate_api_key()
    save_api_key(new_api_key)
    print(f"Generated API Key: {new_api_key}")
