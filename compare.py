import os
from glob import glob
from send2trash import send2trash

def find_and_remove_common_folders(main_folder, other_folders):
    # Obtenir les noms des dossiers enfants du dossier principal
    main_children = set(os.listdir(main_folder))
    identical_folders = set()  # Ensemble pour stocker les noms identiques

    # Comparer avec chaque dossier des autres répertoires
    for folder in other_folders:
        if not os.path.exists(folder):
            print(f"Le dossier {folder} n'existe pas, ignoré.")
            continue

        print(f"Comparaison avec le dossier : {folder}")
        other_children = set(os.listdir(folder))
        # Trouver les noms communs
        common_folders = main_children.intersection(other_children)
        if common_folders:
            print(f"Dossiers identiques trouvés avec {folder} : {common_folders}")
            identical_folders.update(common_folders)
        else:
            print(f"Aucun dossier identique avec {folder}.")

    # Envoyer les dossiers identiques à la corbeille
    for folder_name in identical_folders:
        folder_path = os.path.join(main_folder, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            try:
                send2trash(folder_path)  # Envoie le dossier à la corbeille
                print(f"Dossier envoyé à la corbeille : {folder_path}")
            except Exception as e:
                print(f"Erreur lors de la suppression de {folder_path} : {e}")

    return identical_folders

# Exemple d'utilisation
main_folder = r"./"  # Utilise le répertoire où se trouve le script

# Utilisation de glob pour sélectionner dynamiquement les dossiers "arrivageX"
other_folders = [
    folder for folder in glob("../arrivage*")  # Modèle pour tous les dossiers "arrivageX"
    if os.path.isdir(folder)
]

# Affichage des dossiers trouvés pour comparaison
print("Dossiers trouvés pour comparaison :")
print(other_folders)

# Trouver et supprimer les dossiers identiques
identical_folders = find_and_remove_common_folders(main_folder, other_folders)

# Afficher la liste des dossiers identiques supprimés
if identical_folders:
    print("\nListe des dossiers envoyés à la corbeille :")
    print(identical_folders)
else:
    print("\nAucun dossier identique trouvé dans le dossier principal.")