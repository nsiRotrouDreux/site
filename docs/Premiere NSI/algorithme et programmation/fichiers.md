# Fichiers 

## Concepts clés
- Un fichier = flux de caractères (texte) ou d'octets (binaire).
- Modes courants : `r` (lecture), `w` (écriture, écrase), `a` (ajout), `x` (création), `b` (binaire), `+` (lecture+écriture).
- Toujours fermer un fichier (ou utiliser `with` pour gérer automatiquement la fermeture).
- Encodage courant : `utf-8`.

## Exemples simples

Lire tout le contenu :
La fonction open attend au moins deux arguments : le nom du fichier à traiter et son mode de traitement
```python
with open("notes.txt", "r", encoding="utf-8") as f: #as f : on utilise un alias 
    texte = f.read()
print(texte)
```

Lire ligne par ligne :
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

Écrire dans un fichier (écrase) :
```python
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\nDeuxième ligne\n") # \n permet d'aller à la ligne
```

Ajouter au fichier :
```python
with open("sortie.txt", "a", encoding="utf-8") as f:
    f.write("Ligne ajoutée\n")
```


Lire un fichier `*.csv` avec  le module `csv` :
```python
import csv
with open("table.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.reader(f, delimiter=';')
    for row in lecteur:
        print(row)
```





## Exercices
1. Écrire un programme qui compte le nombre de lignes non vides d'un fichier.
2. Lire un fichier de nombres (un par ligne) et afficher leur somme.
3. Copier seulement les lignes contenant un mot-clé donné dans un nouveau fichier.

