from pathlib import Path

path = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data")

for file in path.iterdir():
    if file.suffix == '.mp3':
        mp3_path = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data/Music")
        if mp3_path.exists():
            mp3_path = mp3_path / file.name
            file.replace(mp3_path)
        else:
            mp3_path.mkdir()
            mp3_path = mp3_path / file.name
            file.replace(mp3_path)

    elif file.suffix == '.jpg':
        jpg_path = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data/Pictures")
        if jpg_path.exists():
            jpg_path = jpg_path / file.name
            file.replace(jpg_path)
        else:
            jpg_path.mkdir()
            jpg_path = jpg_path / file.name
            file.replace(jpg_path)

    elif file.suffix == '.mov':
        mov_path = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data/Movies")
        if mov_path.exists():
            mov_path = mov_path / file.name
            file.replace(mov_path)
        else:
            mov_path.mkdir()
            mov_path = mov_path / file.name
            file.replace(mov_path)
    else:
        others_path = Path("C:/Formation Python Ouriel/Projets/Projet_Trieur_de_Fichiers/Projet_Trieur_de_Fichiers/data/Others")
        if others_path.exists():
            others_path = others_path / file.name
            file.replace(others_path)
        else:
            others_path.mkdir()
            others_path = others_path / file.name
            file.replace(others_path)

print("Finis !")
