import sys
import os
import base64
import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

# Fonction pour dériver une clé d'encryption à partir d'une phrase de passe
def derive_key(password_provided, salt):
    password = password_provided.encode()  # Convert to type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key

def encrypt_file(file_path, key):
    # Encryption logic
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = Fernet(key).encrypt(data)
        encrypted_file_path = file_path + '.stz'
        os.remove(file_path)  # Remove the original file
        with open(encrypted_file_path, 'wb') as f:
            f.write(encrypted)
        messagebox.showinfo("Success", "File encrypted successfully.")
    finally:
        root.destroy()  # Close the window

def decrypt_file(file_path, key):
    # Decryption logic
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = Fernet(key).decrypt(data)
        decrypted_file_path = file_path[:-4]  # Assuming the original file has '.stz'
        os.remove(file_path)  # Remove the encrypted file
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted)
        messagebox.showinfo("Success", "File decrypted successfully.")
    except InvalidToken as e:
        messagebox.showerror("Error", "Failed to decrypt file. The key is incorrect or the file is corrupted.")
    finally:
        root.destroy()  # Close the window


def on_encrypt_button_click():
    process_file(encrypt_file)

def on_decrypt_button_click():
    process_file(decrypt_file)

def process_file(operation):
    seed_phrase = entry.get()
    if seed_phrase:
        salt = b'your_salt_here'  # Use a consistent salt
        key = derive_key(seed_phrase, salt)
        if os.path.isfile(file_path):
            operation(file_path, key)  # Call encrypt or decrypt based on the operation
        else:
            messagebox.showerror("Error", "The file does not exist.")
    else:
        messagebox.showerror("Error", "Seed phrase is required")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        
        root = tk.Tk()
        root.title("File Encryption/Decryption")

        label = tk.Label(root, text="Enter your seed phrase:")
        label.pack()

        entry = tk.Entry(root)
        entry.pack()
        entry.focus_set()

        # Determine whether to show encrypt or decrypt button based on file extension
        if file_path.endswith('.stz'):
            button_text = "Decrypt"
            button_command = on_decrypt_button_click
        else:
            button_text = "Encrypt"
            button_command = on_encrypt_button_click

        # Create a button with the determined text and command
        action_button = tk.Button(root, text=button_text, command=button_command)
        action_button.pack()

        root.mainloop()
    else:
        print("File path argument missing.")
