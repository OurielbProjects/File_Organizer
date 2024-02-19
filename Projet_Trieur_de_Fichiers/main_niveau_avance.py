from pathlib import Path


def organisateur_fichiers(fichier, categorie_dossier):
    destination_dossier = chemin_principal / categorie_dossier
    if not destination_dossier.exists():
        destination_dossier.mkdir()
    destination_fichier = destination_dossier / fichier.name
    fichier.replace(destination_fichier)


chemin_principal = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data/")

for fichier in chemin_principal.iterdir():
    if fichier.is_file():
        if fichier.suffix in (".png", ".jpg"):
            organisateur_fichiers(fichier, "Image")
        elif fichier.suffix in (".mp3", ".mp4"):
            organisateur_fichiers(fichier, "Musique")
        elif fichier.suffix == ".mov":
            organisateur_fichiers(fichier, "Film")
        elif fichier.suffix == ".txt":
            organisateur_fichiers(fichier, "Texte")
        else:
            organisateur_fichiers(fichier, "Autres")
