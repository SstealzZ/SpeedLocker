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
    password = password_provided.encode()  # Convertir en type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Ne peut utiliser le kdf qu'une seule fois
    return key

def encrypt_file(file_path, key):
    # Logique d'encryption
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = Fernet(key).encrypt(data)
        encrypted_file_path = file_path + '.stz'
        os.remove(file_path)  # Supprimer le fichier original
        with open(encrypted_file_path, 'wb') as f:
            f.write(encrypted)
        messagebox.showinfo("Succès", "Fichier encrypté avec succès.")
    finally:
        root.destroy()  # Fermer la fenêtre

def decrypt_file(file_path, key):
    # Logique de déchiffrement
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = Fernet(key).decrypt(data)
        decrypted_file_path = file_path[:-4]  # En supposant que le fichier original a '.stz'
        os.remove(file_path)  # Supprimer le fichier encrypté
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted)
        messagebox.showinfo("Succès", "Fichier déchiffré avec succès.")
    except InvalidToken as e:
        messagebox.showerror("Erreur", "Échec du déchiffrement du fichier. La clé est incorrecte ou le fichier est corrompu.")
    finally:
        root.destroy()  # Fermer la fenêtre

def on_encrypt_button_click():
    process_file(encrypt_file)

def on_decrypt_button_click():
    process_file(decrypt_file)

def process_file(operation):
    seed_phrase = entry.get()
    if seed_phrase:
        salt = b'b96f43b987ae4237780b6494d54986b6e48835da'
        key = derive_key(seed_phrase, salt)
        if os.path.isfile(file_path):
            operation(file_path, key)  # Appeler encrypt ou decrypt en fonction de l'opération
        else:
            messagebox.showerror("Erreur", "Le fichier n'existe pas.")
    else:
        messagebox.showerror("Erreur", "La phrase de passe est requise")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

        if not os.path.isfile(file_path):
            print("Erreur : Le fichier spécifié n'existe pas.")
            messagebox.showerror("Erreur", "Le fichier spécifié n'existe pas.")
            sys.exit(1)

        root = tk.Tk()
        if file_path.endswith('.stz'):
            root.title("Déchiffrer le Fichier")
        else:
            root.title("Chiffrer le Fichier")

        label = tk.Label(root, text="Entrez votre phrase de passe :")
        label.pack()

        entry = tk.Entry(root, width=40, show='*')  # Afficher les caractères de passe comme des étoiles
        entry.pack()

        # Centrer le widget de saisie à l'écran
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_position = (screen_width - entry.winfo_reqwidth()) // 2
        y_position = (screen_height - entry.winfo_reqheight()) // 2
        root.geometry('+{}+{}'.format(x_position, y_position))

        entry.focus_set()

        # Déterminer s'il faut afficher le bouton d'encryptage ou de déchiffrement en fonction de l'extension du fichier
        if file_path.endswith('.stz'):
            button_text = "Déchiffrer"
            button_command = on_decrypt_button_click
        else:
            button_text = "Chiffrer"
            button_command = on_encrypt_button_click

        # Créer un bouton avec le texte et la commande déterminés
        action_button = tk.Button(root, text=button_text, command=button_command)
        action_button.pack()

        # Lier la touche Entrée à la commande du bouton
        root.bind('<Return>', lambda event: action_button.invoke())

        root.mainloop()
    else:
        print("Argument du chemin du fichier manquant.")