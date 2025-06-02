# La dichotomie 


### La méthode

!!! note Quel est le but de l'algorithme et quels sont les prérequis ?

    * Le principe de l'algorithme est de détecter la 
    présence ou non d'un élément dans une liste
    * La liste **est triée par ordre croissant**

!!!

!!! note La méthode 

    Un peu comme au juste prix , on regarde la valeur qui est au milieu de la liste. Si on tombe sur la valeur cherchée , c'est gagné
 
    Si on tombe sur une valeur plus petite que la valeur cherchée, comme la liste est triée, on ne garde que les valeurs situées après le milieu de la liste .

    Si on tombe sur une valeur plus grande que la valeur cherchée, on ne garde que les valeurs situées avant le milieu de la liste .

    <b> Mais quand s'arrête-t-on ?</b>

    On s'arrête bien sur dès que l'on tombe sur la valeur cherchée, en renvoyant <b>True</b> ou alors dès que la liste sur laquelle on travaille ne contient plus d'élément et dans ce cas on renverra <b> False</b>
!!!

### L'algorithme

!!! success  Les variables

    * <b>debut</b> : indice du début de liste
    * <b>fin</b> : indice de la fin de la liste
    * <b>milieu</b> : indice du milieu de la liste obtenue par le calcul :      (debut+fin)//2

       On appelera les paramètres <i><b>liste et valeur </b></i>

!!!
!!! tip A chaque étape


    * On calcule la valeur de l'indice du milieu
    * On compare liste[milieu] et valeur . 
      
         Si valeur est plus petite alors fin prend la valeur milieu -1
     
    
        Si la valeur est plus grande alors debut prend la valeur milieu +1
     
    
        Si la valeur est égale , on renvoie True
!!!

!!! warning Stop ?

    On travaille tant que la valeur n'est pas trouvée ou que debut > fin (cas où il n'y a plus d'élement dans la liste) 
!!!

### Les programmes  
!!! done   "Le programme itératif"

    ```py
    def dichotomie (liste, valeur):
    debut = 0
    fin  = len(liste)
    if liste ==[]:
        return False 
    while debut <= fin:
        m = (debut+fin)//2
        if liste[m]> valeur:
            fin = m-1
        elif liste[m]<valeur:
            debut = m+1
        else :
            return True
    
    return False        
    ```

!!! done " Le programme récursif"
    ```py
    def dichotomie_rec (liste, valeur):
    
        if len(liste)== 0 :
                return False
        m = len(liste)//2
        if liste[m]> valeur:
            return dichotomie_rec(liste[:m],valeur)
        elif liste[m] <valeur :
            return dichotomie_rec(liste[m+1:],valeur)
        else:
            return True
    ```

!!! warning "Un peu de maths
    Combien faut il d'étapes pour avoir la réponse à notre problème avec l'algorithme de dichotomie ?

    On cherche p tel que  n < 2^p^ .

    En effet , on divise à chaque étape la taille de la liste par 2, on compte donc le nombre de fois nécessaires pour que la taille de la liste soit nulle .

    Avec un tout petit peu de maths , on obtient p > $\dfrac{ln(n)}{ln(2)}$ soit log<sub>2</sub>(n)

    Exemple : Pour une liste de taille 100, avec un algorithme de recherche dit de *force brute*, on aurait au pire 100 opérations à rélaiser.

    Avec la méthode de la dichotomie, $\dfrac{ln(100)}{ln(2)}$ = 6.64 à 0.01 près soit 7 opérations.
 