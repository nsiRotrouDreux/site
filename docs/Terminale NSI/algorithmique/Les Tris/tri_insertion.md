# Tri insertion

## Le principe 
!!! warning "Comment ça marche ?"

    On va s'intéresser aux caractéristiques du tri par insertion :
    
    A la première étape , on compare les deux premiers élements de la liste et on les trie pasr ordre croissant

    A la deuxième étape , on  compare le troisième élement avec le deuxième : 

            * S'il est plus grand , on ne change rien.
                                
            * S'il est plus petit, on le compare avec le premier. 
                                         
                 * S'il est plus grand que le premier, on l'insère entre le premier et le second élement
                 * S'il est plus  petit, on le place au premier rang de la liste.
                
                                            
    ....
    
    A la i ème étape, avant de débuter, les i plus petits éléments sont classées par ordre croissant en tête de liste. Il nous reste à trier les n-i derniers éléments.
    
    

!!! success "Invariant de boucle "
    A la i ème étape, les i premiers éléments de la liste sont triés par odre croissant au début de la liste .

    !!! example  "Exemple"
        Soit la liste [5,4,1,0,3]
        Voici l'état de la liste avant et après le tour de boucle. 

        |étape| avant le tour  de boucle| après le tour de boucle|
        |---------|------------------|----------|
        |1|[5,4,1,0,3]|[4,5,1,0,3]|
        |2|[4,5,1,0,3]|[1,4,5,0,3]|
        |3| [1,4,5,0,3]|[0,1,4,5,3]
        |4|[0,1,3,5,4]|[0,1,3,4,5]|

## 2.L'algorithme

```py 
def triInsertion( tab):  # tab=[5,4,1,0,3]
    n = len(tab)
    for i in range(1,n):
        insertion = tab[i]
        j = i-1
        while j >= 0 and insertion <tab[j]: 
            tab[j+1] = tab[j]
            j= j-1
        tab[j+1]  = insertion
        
        print(f" A la fin de la {i+1} ème étape , la liste est  {tab}")
    return tab
    

```
 A la fin de la 1 ème étape , la liste est  [4, 5, 1, 0, 3]

 A la fin de la 2 ème étape , la liste est  [1, 4, 5, 0, 3]

 A la fin de la 3 ème étape , la liste est  [0, 1, 4, 5, 3]

 A la fin de la 4 ème étape , la liste est  [0, 1, 3, 4, 5]


## 3. La complexité
!!! danger " "
    Etudier la complexité d'un programme , c'est étudier son coût en termes de ressource.
    Ce coût dépend bien sur de la taille de objets étudiés. 
    Dans notre cas , on étudie le tri d'une liste dont on ne connait pas la taille . On la note n.

    On parcourt notre liste de l'indice 1 à l'indice n-1 (premiere boucle avec i) puis on utilise un while qui dans le pire des cas va boucler 1 puis 2 puis 3 puis , n-1 fois
    i= 1, on a au pire 1 opération 

    i = 2 on au pire  2 opérations   

    i= n-1 , on a au pire  n-1 opération 


    Soit au total n-1+n-2+n-3+....+4+3+2+1 opérations  soit (n-1)(n)/2 opérations (formule mathématiques). 
    
    On dira que le coût est de l'odre de n² , noté o(n²)

     **La complexité , ici en n², est dite quadratique.**


## A l'épreuve pratique

=== "Sujet"

    ```py
    def tri_insertion(tab):
       '''Trie le tableau tab par ordre croissant
       en appliquant l'algorithme de tri par insertion'''
       n = len(tab)
       for i in range(1, n):
           valeur_insertion = ... 
           # la variable j sert à  déterminer 
           # où placer la valeur à  ranger
           j = ... 
           # tant qu'on n'a pas trouvÃ© la place de l'élément à 
           # insérer on décale les valeurs du tableau vers la droite
           while j > ... and valeur_insertion < tab[...]: 
               tab[j] = tab[j-1]
               j = ... 
            tab[j] = ... 
    ```
=== "Correction"

    ``` py

    def tri_insertion(tab):    
        n = len(tab)
        for i in range(1, n):
            valeur_insertion = tab[i]            
            j = i-1           
            while j > 0 and valeur_insertion < tab[j]: 
               tab[j] = tab[j-1]
               j = j-1 
            tab[j] = valeur_insertion 
    ```