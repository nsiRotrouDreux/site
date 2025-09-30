# Les chaînes de caractères en Python (Première NSI)

## 1. Définition

Une **chaîne de caractères** (ou *string*) est une suite de caractères entourée de guillemets simples `'...'` ou doubles `"..."`.

```python
texte = "Bonjour"
mot = 'Python'
```

## 2. Opérations de base

### a. Accès aux caractères

On peut accéder à chaque caractère d'une chaîne grâce à son indice (le premier caractère a l'indice 0).

```python
texte = "Python"
print(texte[0])  # P
print(texte[2])  # t
```

### b. Parcourir une chaîne

```python
for lettre in texte:
    print(lettre)
```

### c. Longueur d'une chaîne

```python
len(texte)  # 6
```

### d. Concaténation

On peut assembler des chaînes avec `+` :

```python
prenom = "Alice"
nom = "Dupont"
nom_complet = prenom + " " + nom  # "Alice Dupont"
```

### e. Répétition

```python
print("ha" * 3)  # "hahaha"
```

## 3. Quelques méthodes utiles

- `lower()` : met en minuscules
- `upper()` : met en majuscules
- `replace(a, b)` : remplace `a` par `b`
- `find(s)` : cherche la sous-chaîne `s`

```python
s = "Bonjour"
print(s.lower())      # "bonjour"
print(s.upper())      # "BONJOUR"
print(s.replace("o", "a"))  # "Banjaur"
print(s.find("jour")) # 3
```

## 4. Slices (tranches)

Permet d'extraire une partie de la chaîne :

```python
texte = "Premiere NSI"
print(texte[0:8])  # "Premiere"
print(texte[9:])   # "NSI"
```

## 5. Immutabilité

Les chaînes sont **immutables** : on ne peut pas modifier un caractère directement.

```python
texte = "Python"
# texte[0] = "J"  # Erreur !
```

## 6. Exemples d'exercices

1. Afficher chaque lettre d'un mot sur une ligne différente.
2. Compter le nombre de voyelles dans une chaîne.
3. Demander un mot à l'utilisateur et afficher s'il contient la lettre "e".
