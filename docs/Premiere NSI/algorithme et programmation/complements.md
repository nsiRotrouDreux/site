# Compléments : Tuples , liste de listes.
## Concepts rapides
- `tuple` : séquence non mutable, définie avec des parenthèses `(1, 2, 3)`.
- `list` : pour rappe, séquence mutable, définie avec des crochets `[1, 2, 3]`.
- `liste de listes` : structure 2D courante, ex. `[[1,2],[3,4]]`.

!!! warning "Attention"
     Un `tuple` peut contenir des objets mutables (ex. des listes). Le tuple lui‑même ne peut pas être modifié, mais les listes qu’il contient peuvent l'être .

## Exemples


```python
t = (1, 2, 3)
# t[0] = 10  # TypeError: 'tuple' object does not support item assignment
```

Tuple contenant des listes (tuple immuable, éléments mutables)
```python
t = ([1, 2], [3, 4])
# Ici t a deux éléments qui sont chacun une liste .
t[0].append(9)   # autorisé : la liste interne est modifiée
print(t)         # ([1, 2, 9], [3, 4])
# mais : t[0] = [7,8]  # TypeError
```
## Liste de listes (ou tableau, matrice)

| 1| 3    | 2 |
| :--------------- |:---------------:| -----:|
| 5 |  6      |  12|
|16  |4            |  3 |
| -5  |854        |    17|

Pour représenter ce tableau en python , on va utiliser une liste qui aura autant d'éléments qu'il ya de lignes dans le tableau et dont chaque éléments sera une liste contenant les valeurs de la liste.

```python
l = [[1,3,2], [5,6,12],[16,4,3],[-5,854,17]]
l[0][2]     #2
l[1][0]     #5
len(l)      # 4  : nombre de lignes
len (l[0])  # 3  : nombre de colonnes 
```

!!! danger "Attention"

     ```python
     liste = [[0]*10]*10     # On obient une liste de dix listes de dix  0
     liste[1][2]= -5         # L'élément de rang 2 de chaque sous liste prend la valeur -5 
     ```
     En générant la liste , le second *10 ne fait que recopier la première sous liste . On a donc 10 fois la même sous liste et si on en modifie une , on les modifie toutes .

     Pour avoir le résultat voulu :
     ```python
     l =[]
     for i in range (10):
          l.append([0]*10)
      # ou
     l =[[0]*10 for i in range(10)]
     ```


## Quand utiliser quoi ?
- Utiliser `tuple` quand la séquence ne doit pas être réassignée (sécurité / clé dict).
- Utiliser `list` pour structures modifiables (matrices, piles, files).
- Si vous avez un tuple de listes, sachez que seule la structure externe est protégée ; les éléments internes peuvent changer.

