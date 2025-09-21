# La programmation orientée objet


### Introduction

Le titre du chapitre peut faire peur mais pourtant, sans le savoir, vous flirtez constamment depuis le début de la première avec ce concept. 
Historiquement le paradigme objet est apparu dans les années 60 mais a été développé sérieusement à partir des années 70 avec le langage smalltalk. Ce paradigme est aujourd’hui largement répandu parmi les langages ayant le plus de succès.
Mais qu’est-ce donc ?  L’idée est que l’utilisateur puisse utiliser des objets complexes de façon très simple. 
Prenons exemple avec les listes. Vous savez ajouter, enlever, modifier…un élément d’une liste de façon aisée.  Le langage python a mis à notre disposition un objet, les listes, très pratique et facile à utiliser.
Bien évidemment, il a fallu construire cet objet et là, ce n’est plus aussi simple. On va voir comment sur des exemples simples, on peut construire un objet. On va avoir besoin des notions de Classes, attributs, méthodes.

### Classes
Pour créer une classe d’objets, il faut préalablement définir cette classe.
Supposons que nous gérions un parc de voitures pour lesquelles nous voudrions connaitre la couleur, la marque et l’année de mise en circulation.


On va tout d’abord créer l’enveloppe de ces objets à l’aide du mot clé class.
```py 
 class Voiture :
     """ Une classe pour représenter des voitures 
     à l'aide  de leur marque , année , couleur
     """
     pass
v= Voiture()
type(v)

<class '__main__.Voiture'>
``` 
   > **Le nom d'une classe commence toujours par une majuscule**

### Méthode constructeur , attributs.

On a une enveloppe vide pour l'instant. Dans un premier temps, on va définir la méthode constructeur qui a une syntaxe très particulière.

```py 
def __init__ (self, couleur, marque, année):
    self.c = couleur
    self.m = marque
    self.a = année 
```
*Une petite explication ?*

Le nom de la méthode constructeur sera toujours __init__. Ce nom identifiable permet à cette méthode d’être exécutée dès la création d’une instance (ou objet).
Elle a ici quatre paramètres et au minimum en aura un : self
Ce paramètre désigne l’instance (l'objet) à laquelle la méthode sera appliquée. Cela deviendra clair avec quelques exemples.
Les autres paramètres sont facultatifs et désignent les attributs d’instance . Ici , ils ne sont pas définis par défaut. 

!!! success "Résumé"

    Pour définir une classe, il faut tout d'abord lui donner un nom, avec une majuscule . On précèdera ce nom du mot réservé *class*

    On définit ensuite la **méthode constructeur** dont le but est d' affecter les caractéristiques voulues  à chaque objet (instance) de la classe que l'on va créer. Elle s'exécute automatiquement.
    Ici chaque objet recevra une marque, une couleur et une année .
    **c, m, a sont les attributs associés à cette classe** .Couleur , marque, année les **arguments** associés à chaque objet.
    !!! example "Premier exemple"
   
        ```py
        class Voiture:
            def __init__ (self, couleur, marque, année):
                self.c = couleur
                self.m = marque
                self.a = année 
        
        v= Voiture('rouge','Fiat',2015)

        v.c     # v est une instance de la classe Voiture et remplace "self" 
        'rouge'
        v.m
        'Fiat'

        ```
    !!! tip "Remarques sur les attributs"
        
      
        Les valeurs des attributs sont modifiables .
        Par exemple, si l'on repeint la voiture il suffit d'écrire v.c='bleue' pour que l'argument associé à la couleur de l'objet soit bleue.

        Deuxième remaque : On aurait pu ne pas noter les attributs en argument de la méthode constructeur.
        ```py
          class Voiture:
               def __init__ (self):
                   pass
          v= Voiture()
          v.couleur = 'rouge'

        
        ```
        Plus fréquent, les arguments des attributs sont définis par défaut 
        ```py
        class Voiture:
            def __init__ (self, couleur = 'rouge', marque= 'Fiat', année = 2015):
                self.c = couleur
                self.m = marque
                self.a = année 
        
        v= Voiture()

        ```
        On a ici une Fiat rouge de 2015.
        
        


### Les méthodes

Les méthodes ne sont ni plus ni moins que des fonctions définies à l'intérieur d'une classe. Elles ne peuvent être utilisées qu'avec des objets de la classse dont elles dépendent.

Vous connaissez toutes et tous la méthode append  qui s'appliquent aux objets de la classe Liste.

Créeons une méthode qui "repeind" la voiture.

```py
     class Voiture:
           def __init__ (self, couleur, marque, année ):
               self.c = couleur
               self.m = marque
               self.a = année 
            
           def peindre (self, nouvelle_couleur):
               self.c = nouvelle_couleur

     v= Voiture('rouge', 'Fiat', 2015)
     print (f" On a une {v.m} de couleur {v.c}")
     #On a une Fiat de couleur rouge
     v.peindre ('jaune')
     print (f" On a une {v.m} de couleur {v.c}")
     #On a une Fiat de couleur jaune
```
### Une méthode particulière

On a déjà vu la méthode construteur (*def__init__*) on peut aussi la méthode __str__
Cette méthode est utilisée pour permettre un affichage compréhensible des objets à l'aide la fonction print

Regardons la différence d'affichage

```py
     class Voiture:
           def __init__ (self, couleur, marque, année ):
               self.c = couleur
               self.m = marque
               self.a = année 
            
     v= Voiture('rouge', 'Fiat', 2015)
     print(v)
     #<__main__.Voiture object at 0x1256ae0>
```
On est bien avancé ...On a vu plus haut qu'avec un print, on peut afficher les caractéristqiues de l'objet. Mais on peut créer une méthode qui automatise cet affichage 
!!! tip "Le truc en plus"

    ```py
     class Voiture:
           def __init__ (self, couleur, marque, année ):
               self.c = couleur
               self.m = marque
               self.a = année 
            
           def  __str__(self):
               return f" On a une {self.m} de couleur {self.c}"
            
     v= Voiture('rouge', 'Fiat', 2015)
     print(v)
     #On a une Fiat de couleur rouge 
    ```
C'est quand même plus explicite :smirk: