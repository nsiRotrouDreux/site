# Les boucles 

En programmation , on a souvent besoin d'effectuer des taches répétitives. Pour cela on va utiliser des boucles avec deux façons principales de procéder


### While 

Littéralement *tant que* . C'est une instruction que l'on peut utiliser pour un nombre connu d'actions mais surtout lorsque l'on ne sait pas à quel moment il faut sortir de la boucle .

Par exemple , tant qu'il n'est pas midi ( on sait quand cela s'arrête ) ou tant qu'il fait beau ( on connait la cause de l'arrêt mais pas le moment)

!!! danger "Syntaxe de la boucle while"

    Lorsque l'on utilise la boucle while :
     * Il faut penser à initialiser la variable que l'on utilise dans la condition du while.
     * Il faut penser à modifier cette variable dans la boucle sinon , le programme ne s'arrêtera pas.

     !!! example "Exemple"
        ```py
        a= 0
        while a <100:  # on ne connait pas le moment de l'arrêt
            a= a*1.5
        print(a)
         ```
        ```py
        S = 0
        n = 0
        while n<10:  # on connaït exactement le nombre d'itérations.
           S= S+n
           n = n+1
        print(S)
### For

La boucle for est à utiliser quand on connaît le nombre d'itérations à faire.

!!! danger "Le for i in range"


    Tout d'abord , i est une variable que l'on remplacer par n'importe quelle autre lettre, mot , sauf les mots réservés au langage python (str, int , input...)

    Par défaut, il n'y a qu'un paramètre pour la fonction range , celui du nombre d'execution. On commence par défaut à 0 ,avec un pas de 1
    :warning: Si l'on veut afficher, calculer des valeurs jusqu'à un certain rang , il faudra aller jusqu'à celui d'après dans le range.

    !!!example "Exemple"
        
        ```py
        for i in range (10):
            print(i)   # affichage les entiers de 0 à 9
        ```

        ```py
        for i in range (1,11):
            print(i)   # affichage les entiers de 1 à 10
        ```

        ```py
        for i in range (1,11,2):
            print(i)   # affichage les entiers de 1,3,5,7,9
        ```
!!! info "le for comme parcours d'un ensemble"

    Le for peut aussi servir, il le fait très souvent, à parcourir une structure de données ou même une chaïne de caractères .

    ```py
    mot = "zboub"
    for lettre in mot :
        print (lettre)
    
    'z'
    'b'
    'o'
    'u'
    'b'

    ```