# Les listes 

Nous avons présenté dans un premier temps, les types de base (nombre entier ou flottant, caractères, booléens).Il est possible de travailler avec des éléments plus élaborés et notamment ce que l’on appelle des **séquences** .

### Définition

!!! info "Definition"

    Une séquence , en langage python , est un ensemble **ordonné** c'est à dire un ensemble dont on peut accéder aux élements à l'aide d'un indice.

    Les **listes** sont des séquences , ce sont donc donc des ensembles ordonnées dont on peut accéder aux éléments à l'aide d'un indice .

    On peut changer un élément d'une liste : On dit que les listes sont **mutables**

    ```py
    l =[2,3,5,47]
    l[2]=-50
    print(l)
    [2,3,-50,47]
    ```

!!! danger "Les indices en python"
   

    Attention , les indices commencent à 0. Une liste est définie entre [ ]
    Exemple ; l =[1,5,4,7,9] .
    l[0] vaut 1 et 9 correpond au 5 ème élément de la liste , soit l[4].
    ```py
    l=[2,5,7,6,9]
    print(l[2])
    #7
    ```
---
### Génération d'une liste 

Il existe plussieurs façons de générer une liste 


1. En extension 
  l= [1,2,3,4,5]
2. Par compréhension
   l=[ i for i in range(1,6)] # c'est la même liste qu'au dessus
3. Création d'une liste de 10 0
   l =[0]*10

:rainbow: On peut aussi utiliser la fonction range :
list(range(0,10)) renvoie la liste [0,1,2,3,4,5,6,7,8,9]

---
### Parcours d'une liste 

Il existe deux méthodes principales pour parcourir une liste :

  * A l'aide d'un indice :

    ```python
     l= [1,25,3]
     for i in range (3):  # i prend successivement les valeurs 0,1,2
         print(l[i])      # 1 puis 25 puis 3

    ```
  
  * Directement :

   ```python
     l= [1,25,3]
     for elt in l:  # i prend successivement les valeurs 0,1,2
         print(elt)      # 1 puis 25 puis 3

   ```

---
### Opération sur les listes

!!! info "Les méthodes"
     Une méthode est "une sorte de fonctions" qui s'applique à des objets d'un type définies. On va s'intéresser ici à quelques méthodes qui s'appliquent aux listes 

     | Nom de la méthode| Action sur la liste|
     | :--: | :--: |
     | append| ajoute un élément à la fin de la liste|
     | pop| enlève le dernierr élement et le renvoie|
     | pop(i)| enlève l'élément d'indice i|
     |remove(elt) | enlève l'élément elt de la liste|
     | insert (index, valeur ) |insère valeur au rang index de la liste |

    ```py
    # Ajouter un élément : append 
     l= [1,2,3]
     l.append(4)
     print (l)
    [1, 2, 3, 4]

    # retirer le dernier élément : pop
    l.pop()
    4
    print(l)
    [1, 2, 3]

    # supprimer un élément : remove 
    l.remove (2)
    print(l)
    [1,3]

    # insérer un élément à un index donné
    l.insert(1,54)
    print(l)
    [1,54,3]

    # ajouter plusieurs éléments à la fin d'une liste : extend 
    l.extend ([5,6,7])
    print(l)
    [1, 2, 3, 5, 6, 7]

    # Remarque : on peut aussi concatener deux listes 
    l + [123,456]
    print(l)
    l = [1,2,3,5,6,7,123,456]
    ```
:warning: **Un incontournable : len**
  ```py
  # Obtenir la longueur d'une liste : len
  l= [1,2,3]
  len(l)
  3
  ```

  ---
### Tri d'une liste

Avant de vois des algorithmes spécifiques au tri des listes , il existe deux méthodes qui réalisent le travail

  * La méthode sort

  ```py
  # Trier une liste en la modifiant
  l= [10,2,3]
  l.sort()    # l=[2,3,10]
 
  ```

  * La fonction sorted :

```py
  # Trier une liste en la modifiant
  l= [10,2,3]
  ltrie = sorted(l)    # ltrie=[2,3,10] et l =[10,2,3]
 
  ```
  
### Copie d'une liste 

!!! danger "La copie d'une liste"

    ```py
    l=[1,2,3]
    m = l
    l[1] =-17
    print(l)
    [1,-17,3]
    print(m)
    [1,-17,3] 
    ```

    :fearful: m et l représente ici le même objet. Quand on modifie l'un, on modifie l'autre.
    Deux possibilités pour pouvoir garder une copie initiale de la liste

    ```py
    l=[1,2,3]
    m = l[:]   # ou m = list(l)
    l[1] =-17
    print(l)
    [1,-17,3]
    print(m)
    [1,2,3] 
    ```



