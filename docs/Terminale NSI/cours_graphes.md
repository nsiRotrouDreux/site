# 📚 Les graphes – Terminale NSI

## 1. Définition d’un graphe

Un **graphe** est une structure mathématique qui permet de modéliser des relations entre des objets.

Un graphe est composé :
- d’un **ensemble de sommets** (ou nœuds)
- d’un **ensemble d’arêtes** (ou arcs) reliant ces sommets

On note généralement un graphe :  
G = (S, A)

où :
- S est l’ensemble des sommets
- A est l’ensemble des arêtes

---

## 2. Types de graphes

### Graphe non orienté
- Les arêtes n’ont **pas de sens**
- Exemple : réseau d’amis

### Graphe orienté
- Les arêtes ont un **sens**
- Exemple : réseau de followers

---

## 3. Exemples de graphes

### Exemple 1 : graphe non orienté
Sommets :
A, B, C, D

Arêtes :
(A,B), (A,C), (B,D)

### Exemple 2 : graphe orienté
A → B  
A → C  
C → B  

---

## 4. Vocabulaire important

- **Sommet** : élément du graphe
- **Arête** : lien non orienté
- **Arc** : lien orienté
- **Voisin** : sommet relié
- **Degré** : nombre de liens d’un sommet

---

## 5. Liste d’adjacence

Exemple :

A : B, C  
B : A, D  
C : A  
D : B  

---

## 6. Matrice d’adjacence

Exemple :

|   | A | B | C |
|---|---|---|---|
| A | 0 | 1 | 1 |
| B | 1 | 0 | 0 |
| C | 1 | 0 | 0 |

---

## 7. Graphe avec un dictionnaire (Python)

### Graphe non orienté

```python
graphe = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

### Graphe orienté

```python
graphe = {
    "A": ["B", "C"],
    "B": [],
    "C": ["B"]
}
```

---

