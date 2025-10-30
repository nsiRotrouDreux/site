# Slicing 

Le *slicing* est une opération qui permet d'extraire une sous-partie d'une séquence (chaîne, liste, tuple, etc.) en Python.

## Syntaxe
```py
séquence[start:stop:step]
```
- `start` : index de début inclus (par défaut 0).
- `stop`  : index de fin exclus (par défaut len(séquence)).
- `step`  : pas entre éléments (par défaut 1). Peut être négatif.

## Exemples simples
```py
s = "abcdef"
s[1:4]     # 'bcd'    (indices 1,2,3)
s[:3]      # 'abc'    (début → 3)
s[3:]      # 'def'    (3 → fin)
s[::2]     # 'ace'    (tous les 2)
s[::-1]    # 'fedcba' (inverse la séquence)
```

Avec une liste :
```py
L = [0,1,2,3,4,5]
L[2:5]     # [2,3,4]
L[-3:]     # [3,4,5]  (trois derniers éléments)
L[:-2]     # [0,1,2,3]
L[::3]     # [0,3]    (éléments d'indice 0,3,...)
```

## Indices négatifs
Un indice négatif compte depuis la fin : `-1` est le dernier élément. Exemple :
```py
s[-4:-1]   # équivaut à s[len(s)-4:len(s)-1]
```

## Cas particuliers utiles
- Copier une séquence : `copie = seq[:]`
- Prendre les n premiers : `seq[:n]`
- Prendre les n derniers : `seq[-n:]`
- Inverser : `seq[::-1]`


## Remarques
- Le slice retourne une nouvelle séquence 
- Si `start` >= `stop` et `step` positif → slice vide.

