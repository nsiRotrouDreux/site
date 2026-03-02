
# Formulaire HTML - Balises Principales

## Structure de base
On a tous rencontré un formulaire à remplir sur le net. Aujourd'hui, on devient des balaises , le formulaire , c'est nous qui le créons ! :muscle:
Et quand on sera super balaise , on sera même capable de traiter les résultats ... Mais ce n'est pas pour cette année .

Pour info , le traitement d'un formulire se fait coté serveur (on parle de back end par opposition au front end , qui est la partie visible d'un site.)
Le langage utilisé pour récupérer les résultats est le __php__ , c'est un langage qui s'exécute coté serveur .

!!! info   Pour la culture 

     1.	__Envoyer des données sur le web__
     Il existe deux méthodes pour envoyer les données ,  mais le mot clé(attribut)  à utiliser sera toujours method, dans la balise form
     a.	__Methode get__ : elle est peu employée, limitée à 255 caractères et envoie les résultats sur la page courante.
     b.	__Méthode post__ : C’est donc la méthode la plus employée, car elle permet d’envoyer un grand nombre d’informations. De plus, les informations ne sont pas envoyées dans l’adresse de la page 
     2.	__Traiter les données__ :  C’est, toujours dans la balise form, l’attribut action qui va faire le boulot : Par exemple, on va indiquer l’adresse de la page qui va stocker les données. Cela se fait dans un autre langage , le php.
     *La particularité de ce langage est qu’il est exécuté sur le serveur .*
 


__Un formulaire est introduit par la balise form__

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Mon Formulaire</title>
</head>
<body>
    <h1>Formulaire de Contact</h1>
    
    <form action="/traiter" method="POST">
        <!-- Champs du formulaire -->
    </form>
</body>
</html>
```

## Balises principales

| Balise | Description |
|--------|-------------|
| `<form>` | Conteneur du formulaire |
| `<input>` | Champ de saisie (texte, email, password, etc.) |
| `<textarea>` | Zone de texte multiligne |
| `<select>` | Liste déroulante |
| `<option>` | Option dans une liste |
| `<button>` | Bouton d'action |
| `<label>` | Étiquette pour un champ |
| `<fieldset>` | Groupe de champs |
| `<legend>` | Titre d'un groupe |

## Exemple complet

```html
<form action="/contact" method="POST">
    <label for="nom">Nom :</label>
    <input type="text" id="nom" name="nom" required>
    
    <label for="email">Email :</label>
    <input type="email" id="email" name="email" required>
    
    <label for="message">Message :</label>
    <textarea id="message" name="message" rows="5"></textarea>
    
    <button type="submit">Envoyer</button>
</form>
```
## Exercice 
A vous de reproduire la page ci dessous. Vous pouvez , et devez , améliorer la forme grace au fichier css que vous associerez à votre page html.

![alt text](formulaire.png)
