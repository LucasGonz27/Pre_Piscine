import os  # On importe le module os pour travailler avec les dossiers et fichiers

def list_files_recursive(path="."):  # "." signifie le dossier actuel
    # os.walk parcourt tous les dossiers et fichiers du dossier
    for root, dirs, files in os.walk(path):
        print(f"\nDossier : {root}")  # On affiche le dossier courant
        for dir_name in dirs:  # On parcourt tous les sous-dossiers
            print(f"  Dossier  {dir_name}")  # On affiche chaque sous-dossier
        for file_name in files:  # même principe pour les fichiers
            print(f"  Fichier {file_name}")

if __name__ == "__main__":
    list_files_recursive()  # On appelle la fonction sur le dossier actuel