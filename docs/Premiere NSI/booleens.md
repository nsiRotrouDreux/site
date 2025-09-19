# Les Booléens

En informatique, une valeur booléenne est une valeur qui peut prendre deux états , souvent représentés par Vrai ou Faux.

On symbolise souvent ces deux états pour les valeur 1, Vrai  et 0, Faux.

 > En informatique , les booléens sont souvent utiliser dans des tests conditionnels 
``` py
 nombre = int (input("ntrez un nombre :" ))
 if nombre > 10:  # nombre > 10 peut prendre deux valeurs : True ou False 
    print ....
```
### Les opérateurs booléens 
On va établir les tables des principaux opérateurs booléens : **AND**, **OR**, **XOR**, **MOT**

!!! tip "AND"

     | A|B| A AND B|        
     | --- | -- | :--: |
     |0|0|0|
     |0|1|0|
     |1|0|0|
     |1|1|1|         
  AND est vrai si les deux conditions sont vraies.

!!! tip "OR"

     | A|B| A OR B|        
     | --- | -- | :--: |
     |0|0|0|
     |0|1|1|
     |1|0|1|
     |1|1|1|         
   
    OR est vrai si au moins une des deux  conditions est vraie.

!!! tip "XOR"

    | A|B| A XOR B|        
    | --- | -- | :--: |
    |0|0|0|
    |0|1|1|
    |1|0|1|
    |1|1|0|         
   
    XOR est vrai si exctement une condition est vraie.

!!! tip "NOT"

     | A| NOT A|        
     | --- |:--: | 
     |0|1|
     |0|1|
     |1|0|
     |1|0|         
   
    NOT transforme un vrai en faux et inversement


Remarque : OR correspond au ou dans la phrase, j'irai en ville s'il y a un bus ou une voiture er XOR au ou dans la phrase j'irai à la plage ou à la montagne

### Addition et booléen

On peut établir une table où à partir de la valeur des bits, on peut déterminer la somme et la retenue obtenues.

!!! info "addition et booléen"
   
    | A|B| RETENUE|SOMME|        
    | --- | -- | :--: | :---:  |
    |0|0|0|0|
    |0|1|0|1|
    |1|0|0|1|
    |1|1|1|0|

    La retenue correspond à l'opérateur AND et la somme au XOR         

### Python et les booléens

 Les mots clés utilisés en python sont tout à fait naturel 

| Langage naturel|Python|        
| --- | -- | 
|Vrai|True|
|Faux|False|
|Et|AND|
|Ou| OR|
|Ou exclusif|XOR|


### Exercices 

[Lien capytale](https://capytale2.ac-paris.fr/p/basthon/n/?kernel=python3-legacy&mode=create&id=7204983#Exercice-3)