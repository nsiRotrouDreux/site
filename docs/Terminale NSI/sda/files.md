# Les Files en Terminale NSI

Une **file** (ou queue en anglais) est une structure de données linéaire qui fonctionne selon le principe **FIFO** (*First In, First Out*), c'est-à-dire que le premier élément ajouté sera le premier à sortir.

## Principe d'une file

- **Enfiler** (*enqueue*) : ajouter un élément à la fin de la file.
- **Défiler** (*dequeue*) : retirer l'élément en tête de la file.

## Implémentation d'une file avec une liste Python

On part d'une liste vide pour stocker les éléments de la file.

```python
class File:
    def __init__(self):
        self.elements = []

    def est_vide(self):
        return self.elements == []

    def enfiler(self, element):
        self.elements.append(element)

    def defiler(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        return self.elements.pop(0)

    def tete(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        return self.elements[0]

    def __str__(self):
        return str(self.elements)
```

## Exemple d'utilisation

```python
f = File()
f.enfiler(10)
f.enfiler(20)
print(f)         # [10, 20]
print(f.defiler()) # 10
print(f)         # [20]
```

## Point important

- L'opération `defiler` est coûteuse avec une liste Python car elle nécessite de décaler tous les éléments.
