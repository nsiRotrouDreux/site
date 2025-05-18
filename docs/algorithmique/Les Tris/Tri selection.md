# Tri selection

## 1. Le principe 

!!! warning INFO IMPORTANTE

    On va s'intéresser aux caractéristiques du tri par sélection :
    
    A la première étape , on place le plus petit élément de la liste en tête de liste.
    A la deuxième étape , on place le plus petit élément de la liste non triée en tête de liste. Si bien qu'à la fin de cette étape les deux premiers éléments de la liste complète sont les deux plus petits, classés par ordre croissant
    ....
    
    A la i ème étape , avant de débuter, les i-1 plus petits éléments sont classées par ordre croissant en tête de liste. Il nous reste à trier les n-i derniers éléments.
    
    EX  i = 4  l =[0,2,5,9,7,10]. On est au début de la quatrième étape . Il nous reste à classer les 6-4+1=3 derniers éléments 

!!! success "Invariant de boucle "
    A la i ème étape, les i plus petits éléments de la liste sont triés par odre croissant au début de la liste 

    !!! example  "Exemple"
        Soit la liste [5,4,1,0,3]
        Voici l'état de la liste avant et après le tour de boucle. L'algorithme appliqué est celui du *Changement de l'indice*

        |étape| avant le tour  de boucle| après le tour de boucle|
        |---------|------------------|----------|
        |1|[5,4,1,0,3]|[0,4,1,5,3]|
        |2|[0,4,1,5,3]|[0,1,4,5,3]|
        |3| [0,1,4,5,3]|[0,1,3,5,4]
        |4|[0,1,3,5,4]|[0,1,3,4,5]|

## 2. Deux algorithmes 
##### Changement de l'indice
```py 
def triSelection( tab):  # tab=[5,4,1,0,3]
    n = len(tab)
    for i in range(n-1):
        mini = i
        for j in range(i+1):
            if tab[j]< tab[mini]:
                mini =j
        tab[i],tab[mini] = tab[mini],tab[i]
        print(f" A la fin de la {i+1} ème étape , la liste est  {tab}")
    return tab
    

```
A la fin de la 1 ème étape , la liste est  [0, 4, 1, 5, 3]

 A la fin de la 2 ème étape , la liste est  [0, 1, 4, 5, 3]

 A la fin de la 3 ème étape , la liste est  [0, 1, 3, 5, 4]

 A la fin de la 4 ème étape , la liste est  [0, 1, 3, 4, 5]


##### Permutation des valeurs 
``` py 
def TriSelection(t):    # tab=[5,4,1,0,3]
    n = len(t)
    for i in range (n-1):
        mini = t[i]
        for j in range(i+1,n):
            if mini> t[j]:
                mini = t[j]
                t[i], t[j] = t[j],t[i]  
        print(f" A la fin de la {i+1} ème étape , la liste est  {tab}")        
    return t
```
 A la fin de la 1 ème étape , la liste est  [0, 5, 4, 1, 3]

 A la fin de la 2 ème étape , la liste est  [0, 1, 5, 4, 3]

 A la fin de la 3 ème étape , la liste est  [0, 1, 3, 5, 4]

 A la fin de la 4 ème étape , la liste est  [0, 1, 3, 4, 5]

## 3. La complexité
!!! danger " "
    Etudier la complexité d'un programme , c'est étudier son coût en termes de ressource.
    Ce coût dépend bien sur de la taille de objets étudiés. 
    Dans notre cas , on étudie le tri d'une liste dont on ne connait pas la, taille . On la note n.

    On parcourt notre liste de l'indice 0 à l'indice n-2 (premiere boucle avec i) puis on parcourt cette lsite de l'indice i+1 à la fin de la liste .

    i= 0, on a n-1 opérations (j varie de 1 à n-1)

    i = 1 on a n-2 opérations   (j varie de 2 à n-1)


    i= n-2 , on a une opération (j =n-1)


    Soit au total n-1+n-2+n-3+....+4+3+2+1 opérations soit (n-1)(n)/2 opérations (formule mathématiques). 
    
    On dira que le coût est de l'odre de n² , noté o(n²)

     **La complexité , ici en n², est dite quadratique.**
