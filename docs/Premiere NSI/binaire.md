Le binaire

## Ecriture d'un entier en base 2 (ou en binaire)


#### Le système décimal 
Il s’appuie sur 10 symboles :0,1,2,3,4,5,6,7,8,9
Prenons par exemple le nombre 678.
En fait, ce nombre a été construit de la manière suivante : 678= 6*10²+7*10+8
 6 est le chiffre de rang 2 (ou centaine), 7 celui de rang 1 (ou dizaine) et 8 celui de rang 0 ou unités.
Tous les nombres écrits dans le système décimal sont décomposables à l’aide des puissances de 10. Lorsque le rang des unités est plein (à 9), on augmente le rang suivant d’une unité et on réinitialise à 0 le rang qui était plein. Si le rang suivant est lui aussi plein , on réinitialise à 0 les deux rangs et on ajoute 1 au rang suivant, etc…
#### Le système binaire 
Le système binaire s’appuie sur deux symboles, le 0 et le 1 , mais fonctionne exactement comme le système décimal . Dès qu’un rang est plein, on augmente de 1 celui d’après et on réinitialise à 0. Voici la construction de l’écriture des premiers entiers en binaire.

  

|décimal| binaire|       
| :---: | :----: |
| 0     | 0      |
| 1  | 1    |
 | 2  | 10        |
| 3| 11      |
| 4 | 100  |
| 5 | 101        |
| 6| 110      |
| 7 | 111  |
| 8 | 1000 |
| 9| 1001     |
| 10 | 1010  |
       

#### Passage du système décimal au binaire et réciproquement
   
!!!info   "Du décimal au  binaire"
     Il existe une méthode très simple pour passer du décimal au binaire. Cette méthode est fondée sur l’algorithme d’’Euclide et les restes successifs de la division euclidienne par 2 de l’entier que l’on veut convertir. On obtient une succession de reste (0 ou 1) . Il suffit de les écrire du dernier obtenu , qui doit être 1, au premier.
     Exemple : Convertissons 104 en binaire 

    |104| Reste de la division par 2|       
    | :---: | :----: |
     | 104=2*52|0|
       |52=2*26|0|       
       |26=2*13|0|
       |13= 6*2+1|1|
       |6=3*2|0|
       |3=2*1+1|1|
       |1=2*0+1|1|

       L'écriture binaire de 104 s'obtient en écrivant les restes obtenus du dernier au permier soit ici **1101000**

        > Un nombre pair se finira toujours par un 1 en binaire

#### Le binaire sur un octet

 *  L'unité de base en informatqiue est le bit , qui prend donc la valeur 0 ou 1
 * Un octet est composé de 8 bits .
 * Le plus petit nombre que l'on peut écrire sur un octet est 0 et le plus grand 255, qui correspond à 11111111
 * La notation internationale pour l'octet est _o_. On parlera alors de _ko_ (kilooctet), _Mo_ (Megaoctet);_Go_(Gigaoctet)...

  
!!! success "L'astuce pour écrire rapidement un nombre en binaire"  
  
    L'astuce repose sur la connaissance des puissances de 2 , jusqu'à $2^{7}$

     ![alt text](conversionBinaire.png)
     
     [source: siloged.fr](https://siloged.fr/cours/NSI/codage/Changementsdebases.html)

     Il suffit donc de voir si les différentes puissances de 2 "rentre" dans le nombre que l'on veut écrire . Si c'est le cas , on soustrait la;puissance de 2 au nombre à decimal et on reccomence avec la puissance inférieure .

!!! info  "Du binaire au décimal "

     Il peut être utile de savoir que la somme des deux plus grandes puissances,128+64, vaut 192. Ainsi tout nombre entre 192 et 255 aura ses deux bits les plus à gauche (on dit aussi de poids le plus forts ) égaux à 1 en écriture binaire.

     Le passage est plus facile . Il suffit d'additionner les puissances de 2 dont le bit correspondant en bianire est 1.

    !!! example 
          01011010 : 0x128+1x64+0x32+1x16+1x8+0x4+1x2+0x1 =90
          
          Easy  :muscle: