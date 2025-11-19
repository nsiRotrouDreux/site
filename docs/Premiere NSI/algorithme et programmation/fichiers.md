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
Autre méthode , sans with

``` python
f = open("notes.txt", "r", encoding="utf-8") 
texte = f.read()
print(texte)
f.close()

```

Lire ligne par ligne :
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```
ou utiliser la méthode readline , qui ne lit qu'une ligne 
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    f.readline()
```

lLire et stocker chaue ligne dans une liste ; méthode readlines()
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    f.readlines()
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

* On importe chaque enregistrement dans une liste.
```python
import csv
with open("table.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.reader(f, delimiter=';')
    for row in lecteur:
        print(row)
```
* On importe les données de chaque enregistrement dans un dictionnaire : En clés les descripteurs, en valeur la donnée correpsondante.



```python
import csv
with open("table.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.DictReader(f, delimiter=';')
    for row in lecteur:
        print(row)
```
Exportation dans un fichier csv

```python
# Créer une liste pour les en-têtes
en_tete = ["titre", "description"]

# Créer un nouveau fichier pour écrire dans le fichier appelé « data.csv »
with open('data.csv','w') as fichier_csv:
    # Créer un objet writer (écriture) avec ce fichier
    writer = csv.writer(fichier_csv, delimiter=';')
    writer.writerow(en_tete)                         # Les clés de notre dictionnaire deviennent les descripteurs de notre fichier csv.
    pass                                             # Dépend de la forme de la structure sur laquelle on travaille.
    
```

## Exercices
1. Écrire un programme qui compte le nombre de lignes non vides d'un fichier.
2. Lire un fichier de nombres (un par ligne) et afficher leur somme.
3. Copier seulement les lignes contenant un mot-clé donné dans un nouveau fichier.

