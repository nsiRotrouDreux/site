# Cours : Les dictionnaires Python — Première NSI

## Qu'est‑ce qu'un dictionnaire ?
- Un dictionnaire est une structure de données associant des clés à des valeurs.
Les clés ne sont pas accessibles à l'aide d'un indice , les dictionnaires ne sont donc pas de séquences.
- Les clés sont uniques et immuables tandis que les valeurs sont de n'importe quel type
- Syntaxe : `{"clé": valeur, ...}`

## Création et accès
```python
d = {"nom": "Alice", "age": 17}
print(d["nom"])          # "Alice"
print(d.get("ville"))    # None (évite KeyError) 
print(d.get("ville", "inconnue"))  # "inconnue"
```

## Ajouter / modifier / supprimer
```python
d["ville"] = "Paris"     # ajout ou modification
d["age"] = 18            # modification de la valeur 
d.update({"age": 18})    # met à jour plusieurs paires
d.pop("age")             # supprime et retourne la valeur
del d["nom"]             # supprime la clé (KeyError si absente)
d.clear()                # vide le dictionnaire
```

## Parcourir un dictionnaire
```python
for k in d:              # parcourt les clés
    print(k, d[k])

for k, v in d.items():   # clés et valeurs
    print(k, v)

for v in d.values():     # seules les valeurs
    print(v)
```



## Création par compréhension d'un dictionnaire.
```python
carrés = {i: i*i for i in range(6)}  # {0:0, 1:1, 2:4, ...}
```

## Dictionnaires imbriqués
- Les valeurs d'un dictionnaire peuvent être de n'importe quel type... et notamment un dictionnaire.
- Cela permet de représenter des objets plus complexes (par ex. annuaire).
```python
annuaire = {
  "alice": {"age": 17, "ville": "Lyon"},
  "bob": {"age": 18, "ville": "Paris"}
}
print(annuaire["alice"]["ville"])  # "Lyon"
   
```

!!! warning "Attention"
    - Les clés doivent être immuables (listes non autorisées).
    - `d1 = d2` crée une référence ; utiliser `copy()` pour dupliquer.
    - L'ordre des éléments est préservé depuis Python 3.7 

## Exemple 
- Compter les lettres d'une chaîne :
```python
s = "banana"
compte = {}
for c in s:
    if c in compte:
        compte[c] = compte[c]+1
    else:
        compte[c] = 1
    
# {'b':1, 'a':3, 'n':2}
```

