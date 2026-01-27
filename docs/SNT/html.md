# Fiche synthèse — Commandes HTML importantes

Cette fiche présente les balises HTML essentielles avec de courts exemples pratiques.
Elle est destinée aux débutants comme aide-mémoire rapide.

---

## Structure de base

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8">
    <title>Mon site</title>
  </head>
  <body>
    Contenu de la page
  </body>
</html>
```

---

## Texte et titres

```html
<h1>Titre principal</h1>
<h2>Sous-titre</h2>
<p>Ceci est un paragraphe.</p>
<strong>Texte important</strong>
<em>Texte en italique</em>
```

---

## Liens et images

```html
<a href="https://www.example.com">Lien vers un site</a>

<img src="image.jpg" alt="Description de l'image">
```

---

## Listes

```html
<ul>
  <li>Élément 1</li>
  <li>Élément 2</li>
</ul>

<ol>
  <li>Premier</li>
  <li>Deuxième</li>
</ol>
```

---

## Tableaux

```html
<table>
  <tr>
    <th>Nom</th>
    <th>Âge</th>
  </tr>
  <tr>
    <td>Alice</td>
    <td>25</td>
  </tr>
</table>
```

---

## Formulaires

```html
<form action="/traitement" method="post">
  <label>Nom :</label>
  <input type="text" name="nom">

  <input type="submit" value="Envoyer">
</form>
```

---

## Balises sémantiques HTML5

```html
<header>En-tête</header>
<nav>Menu</nav>
<main>Contenu principal</main>
<section>Section</section>
<article>Article</article>
<footer>Pied de page</footer>
```

---

## Multimédia

```html
<audio controls>
  <source src="son.mp3" type="audio/mpeg">
</audio>

<video controls width="300">
  <source src="video.mp4" type="video/mp4">
</video>
```

