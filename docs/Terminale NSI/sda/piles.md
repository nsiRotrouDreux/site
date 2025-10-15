# Les piles 

## Définition

Une **pile** est une structure de données qui fonctionne selon le principe **LIFO** (*Last In, First Out*), c'est-à-dire que le dernier élément ajouté est le premier à être retiré.

## Opérations principales

- **empiler (push)** : ajouter un élément au sommet de la pile.
- **dépiler (pop)** : retirer l’élément au sommet de la pile.
- **sommet (top/peek)** : accéder à l’élément au sommet sans le retirer.
- **est_vide (is_empty)** : vérifier si la pile est vide.

On implémente la pile à l'aide d'une liste vide

## Exemple de codage en Python

```python
class Pile:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return len(self.elements) == 0

    def empiler(self, element):
        self.elements.append(element)

    def depiler(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.elements.pop()

    def sommet(self):
        if self.est_vide():
            raise IndexError("La pile est vide")
        return self.elements[-1]
```

## Exemple d'utilisation

```python
p = Pile()
p.empiler(5)
p.empiler(10)
print(p.sommet())  # Affiche 10
print(p.depiler()) # Affiche 10
print(p.depiler()) # Affiche 5
print(p.est_vide()) # Affiche True
```

## Applications des piles

- Annulation/rétablissement dans les éditeurs de texte
- Évaluation d'expressions arithmétiques
- Parcours en profondeur (DFS) dans les graphes
