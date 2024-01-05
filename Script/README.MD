# Script Folder Documentation

## Overview

This folder contains the `SpeedLocker` script responsible for encrypting and decrypting files using a passphrase. It's designed to be a straightforward tool for handling sensitive data with secure encryption.

## Files

- `encrypt_gestion.py`: The main script for the encryption and decryption process.

## How it Works

`encrypt_gestion.py` utilizes Python's `cryptography` library to encrypt and decrypt files. It provides a simple GUI for user interaction.

### Key Functions

- `derive_key(password_provided, salt)`: Creates a secure key from the provided passphrase and salt.
- `encrypt_file(file_path, key)`: Encrypts the target file and saves it with a `.stz` extension.
- `decrypt_file(file_path, key)`: Decrypts the target `.stz` file back to its original format.

## Dependencies

- Python 3.x
- Cryptography library
- Tkinter (for GUI)

## Setup and Execution

To set up and run the script:

1. Ensure all dependencies are installed.
2. Run the script via command line or an IDE capable of handling Python scripts.

In [Installation.bat](Installation.bat), it's the script to install the script in right click menu. Change the path to your custom version of python if is not the same as mine.

## Usage

To use the script:

1. Start the script with Python.
2. Enter the file path as an argument.
3. Use the GUI to enter the passphrase and select whether to encrypt or decrypt.

## Development and Contributions

This script is open for improvements and contributions. Please ensure any contributions are well-documented and tested.

## Contact

For any queries or contributions, please contact me.

