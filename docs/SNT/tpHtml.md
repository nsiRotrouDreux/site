## Semaine 1

Vous créez votre site à partir du code déjà donné 
```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Vous mettez un titre à cette page</title>
</head>
<body>
 /*  Vous téléchargez votre image (largeur 1800px) , vous pouvez l'appeler .Ici elle s'appelle image.jpg       /*
  <header><img src="image.jpg" alt="Description de l'image"></header>
    
 <footer> Vous ajoutez votre Nom et Prénom et votre classe</footer> 
</body>
</html>
```
### Mise en page 
Pour que votre page s'affiche correctement, il faut faire un peu de ... mise en page : Pour cela on utilise une feuille de style qui est un fichier css. On gère notamment:

   * La police
   * Les couelurs du texte , de fond
   * L'apparence des liens url, quand on passe dessus, une fois visité
   * Les bordures 
   * L'agencement des divers éléments
   etc 

   Vous avez plein d'indications dans [le cours sur le css ](css.md).

!!! example Exemple de codes css sur le footer


    ```css
         footer {
          width:100%; /* occupe toute la largeur de la page */
          border-radius: 20px; /* à adapter : Pour arrondir la bordure*/
          background-color:blue; 
          color: yellow;
    
          font-size:1.5em; /* adapte la taille de l'écriture */
          }
    ```

### Semaine 2 voire 3 au rythme où ça va

Le but est de créer deux zones de texte séparées mais alignées horizontalement

![alt text](dom.png)

Vous avez ci dessus le modèle que l'on veut obtenir.
Toutes le "cases " dépendent de body. Donc tout ce que vous rentrez comme valeur dans l'attribut body du fichier css sera pasr défaut appliqué à tous les éléments qui en dépendent. 
Par exmemple une couleur de fond.
Pour modifier la couleur de fond du contenu de l'élément' article, il faut dans le css ajouter une couleur **dans l'attribut** article.

De la même façon article et aside dépendent de main.

 1. Vous devez  compléter le css pour que main occuppe 100% de la largeur 

```css
    main{    /* ici on gère l'alignement horizontal des éléments*/
     display: flex;
     align-items: flex-start;
     justify-content: space-between;
     width:...;
   }


  article {
    width ...; 
   
   }


 aside{
  width:30%....; 
 
 }
/* ici on gère l'aspect des liens sur le site */
  a {
  outline: none;
  text-decoration: none;
  padding: 2px 1px 0;
  font-family: calibri;
  
  }
  a :link {
    color: ...;
  }

  a:visited {
  color: ....;
 }

  a:focus {
  border-bottom: 1px solid;
  background: .....;
 }

  a:hover {
  border-bottom: 1px solid;
  background: ......;
    ;
}
```


 2. Vous devez compléter les margeurs des balises article et aside en définissant en pourcentage l'espace en largeur que vous voulez que ces balises occupent.
 3.  :fire: Si vous ne laissez pas d"'espace ntre les différents éléments, "tout" va être collé 

Voici quelques indications sur deux attributs css que vous pouvrez utilisez 

!!! tip Le margin

     Le margin est un espace entre la boite et les autres éléments de la page 
     ![alt text](margin.png)

     Vous pouvez différencier les écarts avec les attributs margin-top (-left, -right,-bottom)


!!!tip Le padding
      Le padding est un espace entre la boite et son contenu  
     ![alt text](padding.png)
     
     Vous pouvez différencier les écarts avec les attributs padding-top (-left, -right,-bottom)
    
**La principale différence entre padding et margin est que margin affecte l’espace entourant un élément, tandis que padding contrôle l’espace à l’intérieur d’un élément.**