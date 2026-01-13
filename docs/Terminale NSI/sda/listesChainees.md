# Listes chainées 
## Introduction
![alt text](<c:/Users/Bruno/Documents/bruno/Site/docs/Terminale NSI/sda/lc.png>)
Une liste chaînée est une structure de données où chaque élément (nœud) contient une valeur et une référence vers le nœud suivant.

## Structure d'un nœud

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Avantages et inconvénients

| Avantage | Inconvénient |
|----------|-------------|
| Insertion/suppression O(1) | Accès aléatoire impossible |
| Taille dynamique | Mémoire supplémentaire (pointeur) |
| Pas de réallocation | Complexité de parcours O(n) |

## Opérations principales

### Insertion
```python
def insert(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Recherche
```python
def search(self, target):
    current = self.head
    while current:
        if current.data == target:
            return True
        current = current.next
    return False
```

### Suppression
```python
def delete(self, data):
    if self.head.data == data:
        self.head = self.head.next
        return
    current = self.head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return
        current = current.next
```

## Cas d'usage

- Implémentation de piles et files d'attente
- Graphes et arbres
- Gestion de mémoire dynamique