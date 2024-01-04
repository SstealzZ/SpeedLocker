import sys
import tkinter as tk
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    # Votre logique d'encryption ici
    pass

# Générer ou récupérer une clé d'encryption
key = Fernet.generate_key()

if __name__ == "__main__":
    # Récupérer le chemin du fichier depuis les arguments de ligne de commande
    file_path = sys.argv[1]

    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Encryption in Progress...")

    # Afficher le nom du fichier
    label = tk.Label(root, text=f"Encrypting file: {file_path}")
    label.pack()

    # Exécutez la fenêtre
    root.after(1000, lambda: root.destroy())  # Ferme la fenêtre après 1 seconde
    root.mainloop()

    # Après la fermeture de la fenêtre, continuez avec l'encryption
    encrypt_file(file_path, key)
