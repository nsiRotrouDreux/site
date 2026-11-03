# TP Filius : interconnexion de réseaux et serveur web

**Niveau :** SNT / NSI / SIN\
**Durée :** 1 h 30 à 2 h\
**Logiciel :** Filius\
**Nom, prénom :** ........................................  **Classe :** ..............

## Objectifs

- Attribuer des adresses IP, un masque et une passerelle à des machines.
- Configurer les interfaces d’un routeur pour relier deux réseaux.
- Tester la communication avec la commande `ping`.
- Installer et utiliser un serveur web et un navigateur sur un réseau simulé.

## Rappels

- Une **adresse IP** identifie une machine sur un réseau (ex. `192.168.1.10`).
- Le **masque de sous-réseau** indique quelle partie de l’adresse désigne le réseau. Ici : `255.255.255.0`, donc les trois premiers nombres identifient le réseau.
- Deux machines communiquent directement si elles sont dans le **même réseau**.
- Pour joindre une machine d’un **autre réseau**, la machine envoie ses paquets à sa **passerelle** : l’adresse IP de l’interface du routeur située dans son propre réseau.
- Un **routeur** possède **une adresse IP par réseau auquel il est connecté**.

---

## Exercice 1 : connecter deux réseaux et faire un ping

### Plan d’adressage à compléter

On souhaite construire le schéma suivant :

- **Réseau A** : `192.168.1.0/24`, avec deux ordinateurs (PC1 et PC2) reliés à un switch.
- **Réseau B** : `192.168.2.0/24`, avec deux ordinateurs (PC3 et PC4) reliés à un autre switch.
- Un **routeur** relie les deux switchs.

**Question 1.** Complétez le tableau d’adressage. Choisissez des adresses valides et différentes pour chaque machine. Par convention, l’interface du routeur prend l’adresse `.254` dans chaque réseau.

| Équipement | Réseau | Adresse IP | Masque | Passerelle |
| --- | --- | --- | --- | --- |
| PC1 | A | ................ | ................ | ................ |
| PC2 | A | ................ | ................ | ................ |
| PC3 | B | ................ | ................ | ................ |
| PC4 | B | ................ | ................ | ................ |
| Routeur, interface côté A | A | ................ | ................ | sans objet |
| Routeur, interface côté B | B | ................ | ................ | sans objet |

**Question 2.** Pourquoi PC1 et PC3 n’ont-ils pas la même passerelle ?

..............................................................................................

### Réalisation dans Filius

1. Lancez Filius. Vous êtes en **mode conception** (icône marteau).
2. Placez sur la zone de travail : 4 ordinateurs, 2 switchs et 1 routeur.
3. Reliez avec des câbles : PC1 et PC2 au switch 1 ; PC3 et PC4 au switch 2 ; le switch 1 au routeur ; le switch 2 au routeur.
4. Double-cliquez sur chaque **ordinateur** et renseignez son adresse IP, son masque et sa passerelle d’après votre tableau.
5. Double-cliquez sur le **routeur** : dans l’onglet des connexions, renseignez l’adresse IP et le masque de chaque interface (une par réseau, selon le câble auquel elle correspond).
6. Enregistrez votre travail (`Fichier > Enregistrer`) sous le nom `tp1_NOM.fls`.

### Test de la connexion

1. Sur PC1, double-cliquez sur l’ordinateur, choisissez **Installation de logiciels**, installez la **Ligne de commande**, puis appliquez les modifications.
2. Passez en **mode simulation** (icône triangle vert).
3. Ouvrez la ligne de commande de PC1 et testez :
   - `ping` vers PC2 (même réseau) ;
   - `ping` vers l’interface du routeur côté A ;
   - `ping` vers PC3 (autre réseau).

**Question 3.** Notez les résultats.

| Test | Réussi ? (oui / non) |
| --- | --- |
| PC1 vers PC2 | ................ |
| PC1 vers routeur (côté A) | ................ |
| PC1 vers PC3 | ................ |
| PC1 vers PC4 | ................ |

**Question 4.** Si le ping vers PC3 échoue, listez les points à vérifier.

..............................................................................................

**Question 5 (réflexion).** Modifiez la passerelle de PC1 en une adresse incorrecte puis refaites un ping vers PC3. Que constatez-vous ? Que prouve cette expérience sur le rôle de la passerelle ?

..............................................................................................

---

## Exercice 2 : héberger un site web et le consulter depuis un autre réseau

### Objectif

Une machine du réseau A joue le rôle de **serveur web**. Une machine du réseau B utilise un **navigateur** pour afficher la page hébergée.

On reprend le montage de l’exercice 1 (enregistrez-le d’abord sous `tp2_NOM.fls`).

### Étape 1 : installer les logiciels

En **mode conception**, double-cliquez sur la machine concernée, puis **Installation de logiciels** et appliquez les modifications :

- Sur **PC2** (réseau A) : installez le **Serveur web** et l’**Éditeur de texte**.
- Sur **PC3** (réseau B) : installez le **Navigateur web**.

**Question 6.** Quelle est l’adresse IP de la machine qui sert de serveur ? ................

### Étape 2 : créer la page web

1. Passez en **mode simulation**.
2. Sur PC2, ouvrez l’**Éditeur de texte** et choisissez `Fichier > Ouvrir`. Dans le dossier `webserver`, ouvrez le fichier `index.html`.
3. Remplacez son contenu par votre propre page, par exemple :

```html
<html>
  <head><title>Mon site Filius</title></head>
  <body>
    <h1>Bonjour depuis le serveur !</h1>
    <p>Page créée par : (votre nom)</p>
  </body>
</html>
```

4. Enregistrez le fichier (`Fichier > Enregistrer`).

### Étape 3 : démarrer le serveur

1. Sur PC2, ouvrez le **Serveur web**.
2. Cliquez sur **Démarrer**. Le serveur est alors en écoute.

### Étape 4 : consulter le site

1. Sur PC3, ouvrez le **Navigateur web**.
2. Dans la barre d’adresse, saisissez l’adresse IP du serveur : `http://` suivie de l’adresse de PC2.
3. Validez : votre page doit s’afficher.

**Question 7.** Faites une capture d’écran du navigateur de PC3 affichant la page, et collez-la ci-dessous ou rendez-la avec votre fichier.

**Question 8.** Quel chemin suivent les paquets entre PC3 et le serveur ? Citez dans l’ordre les équipements traversés.

..............................................................................................

**Question 9.** Que se passe-t-il si vous arrêtez le serveur web sur PC2 puis actualisez la page sur PC3 ? Pourquoi ?

..............................................................................................

### Pour aller plus loin (facultatif)

- Modifiez le texte de la page sur PC2 et vérifiez que PC3 affiche la nouvelle version après actualisation.
- Ajoutez un deuxième réseau C relié au même routeur (par exemple `192.168.3.0/24`) avec un PC, et affichez le site depuis ce nouveau réseau.
- Installez un **serveur DNS** et associez un nom (par exemple `www.monsite.fr`) à l’adresse du serveur web.

---

## Barème indicatif (/20)

| Critère | Points |
| --- | --- |
| Tableau d’adressage cohérent (Q1) | 4 |
| Schéma Filius correct et enregistré | 3 |
| Ping inter-réseaux réussi et analysé (Q3 à Q5) | 5 |
| Serveur web opérationnel, page personnalisée | 4 |
| Page affichée depuis l’autre réseau et réponses Q8, Q9 | 4 |

---


