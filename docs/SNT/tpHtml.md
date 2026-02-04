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