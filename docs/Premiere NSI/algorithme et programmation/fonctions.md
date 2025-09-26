# Les Fonctions en Python

## Qu'est-ce qu'une fonction ?

Une **fonction** est un bloc de code qui réalise une tâche précise. Elle permet de réutiliser du code sans le réécrire.

## Pourquoi utiliser des fonctions ?

- **Réutilisation** : écrire une fois, utiliser plusieurs fois.
- **Lisibilité** : le code est plus clair et organisé.
- **Modularité** : chaque fonction a un rôle précis.

## Définir une fonction

Pour créer une fonction en Python, on utilise le mot-clé `def` :

```python
def nom_de_la_fonction():
    # instructions
```

Exemple :

```python
def dire_bonjour():
    print("Bonjour !")
```

## Appeler une fonction

Pour exécuter une fonction, il suffit d'écrire son nom suivi de parenthèses :

```python
dire_bonjour()
```

## Les paramètres

On peut donner des **paramètres** à une fonction pour qu'elle soit plus flexible :

```python
def saluer(prenom):
    print("Bonjour", prenom)
```

Appel avec un paramètre :

```python
saluer("Alice")
saluer("Bruno")
```

## La valeur de retour

Une fonction peut **renvoyer** une valeur avec le mot-clé `return` :

```python
def carre(x):
    return x * x
```

Utilisation :

```python
resultat = carre(5)
print(resultat)  # Affiche 25
```

## La documentation
 Il peut être utile de commenter une fonction en expliquant ce qu'elle fait, le type des paramètres, ce qu'elle renvoie... On parle de **docstring**

```py
def carre(x):
    """ Cette fonction renvoie le carré d'un nombre passé en paramètre
    entrée : Un entier x
    sortie : le carré de ce nombre
    """
    return x*x
```
## Différence entre le print et le return
Voici la différence entre `print` et `return` dans une fonction Python :

- **`print`** affiche une information à l'écran (dans la console par exemple). Il sert à communiquer avec l'utilisateur ou à déboguer.
- **`return`** renvoie une valeur à l'endroit où la fonction a été appelée. Cette valeur peut être utilisée dans d'autres calculs ou stockée dans une variable.

Exemple :

````python
def affiche_somme(a, b):
    print(a + b)  # Affiche le résultat, mais ne le renvoie pas

def calcule_somme(a, b):
    return a + b  # Renvoie le résultat, utilisable ailleurs

# Utilisation
affiche_somme(2, 3)      # Affiche 5, mais ne retourne rien
resultat = calcule_somme(2, 3)
print(resultat)           # Affiche 5, car resultat vaut 5
````



## À retenir :

- Une fonction s'écrit avec `def`.
- On peut lui donner des paramètres.
- On peut documenter la fonction afin d'expliquer ce qu'elle fait.
- On peut utiliser `return` pour renvoyer une valeur.
- Les fonctions rendent le code plus clair et réutilisable.
- Utilisez `print` pour afficher.
- Utilisez `return` pour transmettre une valeur à l'extérieur de la fonction.

