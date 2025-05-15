# La décidabilité

## Introduction au problème

On va étudier les possibilités et les limites des algorithmes. 
Pour cela , on va considérer des programmes qui prennent comme données d'autres programmes . 

!!! tip  " Exemple "
    On crée un petit programme python, que l'on va executer. On le donne au programme python qui va l'interpréter , 
    par exemple en ligne de commande . Le nom du programme est test.py
     
    ``` python  title="test.py"

      for i in range (5):
         print (f" valeur de i  = {i}")

    ```
     ![sortie test(5)](images/res_test.png)   


## La décidabilité

!!! abstract "Définition"
    On dit d'un problème qu'il est décidable si l'on peut répondre par oui ou par non à la question qu'il pose .
    Dans le cas contraire , le problème est dit <i>indécidable</i> .
    Si un problème est décidable , il existe un algorithme qui peut le résoudre .

    Rappel : Un algorithme est une <b>suite finie</b> d'instructions 

!!! example "Un exemple" 
    
    Existe -t-il un programme qui soit capable de calculer la somme des n premiers entiers positifs, n étant passé en paramètre ?...oui :smile:
    
    ``` python 

         def somme (n):
             S = 0
             for i in range (1,n+1):
                 S = S+i
             return S

    ```