# 📄 Page Markdown – Quelques balises et bases importantes en CSS

Cette page est un petit aide‑mémoire en **Markdown** présentant des balises HTML courantes et des propriétés CSS essentielles, avec exemples.

---

## 1. Balises HTML fréquemment stylées

```html
<div>Conteneur générique</div>
<p>Paragraphe</p>
<h1>Titre principal</h1>
<a href="#">Lien</a>
<img src="image.png" alt="Image" />
<button>Bouton</button>
```

---

## 2. Sélecteurs CSS importants

```css
/* Sélecteur par balise */
p { color: black; }

/* Sélecteur par classe */
.card { padding: 16px; }

/* Sélecteur par id */
#main { max-width: 800px; }

/* Sélecteur descendant */
nav a { text-decoration: none; }

/* Pseudo‑classe */
a:hover { color: red; }
```

---

## 3. Propriétés CSS essentielles

### Mise en page (layout)

```css
display: block | inline | flex | grid;
position: static | relative | absolute | fixed;
margin: 10px;
padding: 10px;
width: 100%;
height: auto;
```

### Texte et typographie

```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
line-height: 1.5;
text-align: center;
```

### Couleurs et arrière‑plans

```css
color: #333;
background-color: #f5f5f5;
background-image: url("bg.png");
```

### Bordures et arrondis

```css
border: 1px solid #ccc;
border-radius: 8px;
```

### Effets visuels

```css
box-shadow: 0 2px 8px rgba(0,0,0,0.1);
opacity: 0.8;
transition: all 0.3s ease;
```

---

## 4. Exemple simple HTML + CSS

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
    }

    .card {
      background: white;
      padding: 20px;
      margin: 40px auto;
      max-width: 400px;
      border-radius: 10px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    .card h2 {
      color: #2c3e50;
    }

    .card button:hover {
      background-color: #3498db;
      color: white;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2>Carte exemple</h2>
    <p>Ceci est un exemple simple de mise en forme CSS.</p>
    <button>Cliquer</button>
  </div>
</body>
</html>
```

---

## 5. Mini‑mémo rapide

- `display: flex` → alignement moderne
- `margin` / `padding` → espacements
- `.classe` / `#id` → ciblage précis
- `:hover` → interaction utilisateur
- `box-shadow` + `border-radius` → cartes modernes

---

✏️ Tu peux utiliser cette page comme base de cours, fiche de révision ou documentation Markdown sur le CSS.

