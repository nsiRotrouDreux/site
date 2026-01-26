
# Principales lignes de commande et notions de chemins sous LINUX



## 1. Le terminal et le shell

Sous Linux, on interagit souvent avec le système via un **terminal** et un **shell** (souvent `bash` ou `zsh`).
Chaque commande a la forme générale :

```bash
commande [options] [arguments]
```

Exemple :
```bash
ls -l /home/user
```

---

## 2. Commandes essentielles

### 2.1 Navigation dans les répertoires

| Commande | Description | Exemple |
|----------|-------------|---------|
| `pwd` | Affiche le répertoire courant | `pwd` |
| `ls` | Liste le contenu d’un dossier | `ls` , `ls -l` , `ls -a` |
| `cd` | Change de répertoire | `cd /home/user` , `cd ..` |

Rappels utiles :
- `.` = répertoire courant
- `..` = répertoire parent   : on remonte dans l'arborescence 
- `~` = répertoire personnel (home)

---

### 2.2 Manipulation de fichiers et dossiers

| Commande | Description | Exemple |
|----------|-------------|---------|
| `touch` | Crée un fichier vide | `touch notes.txt` |
| `mkdir` | Crée un dossier | `mkdir projets` |
| `rm` | Supprime un fichier | `rm notes.txt` |
| `rm -r` | Supprime un dossier et son contenu | `rm -r test` |
| `cp` | Copie un fichier ou dossier | `cp a.txt b.txt` , `cp -r dir1 dir2` |
| `mv` | Déplace ou renomme | `mv old.txt new.txt` |
 
:boom: Exemple de copie d'un fichier 
```text
cp  documents/cours.txt  images
```
On copie, depuis le répertoire alice le fichier cours.txt qui est dans le réperoire document et on place la copie dans le répertoire images.
---

### 2.3 Consultation de fichiers

| Commande | Description | Exemple |
|----------|-------------|---------|
| `cat` | Affiche le contenu | `cat fichier.txt` |
| `less` | Affichage paginé | `less fichier.txt` |
| `head` | Début du fichier | `head -n 10 fichier.txt` |
| `tail` | Fin du fichier | `tail -n 10 fichier.txt` |

---

### 2.4 Aide et informations

| Commande | Description | Exemple |
|----------|-------------|---------|
| `man` | Manuel d’une commande | `man ls` |
| `--help` | Aide rapide | `ls --help` |

---

## 3. Arborescence simple de fichiers

Exemple d’arborescence :

```
/
├── home
│   └── alice
│       ├── documents
│       │   └── cours.txt
│       └── images
│           └── photo.jpg
└── etc
    └── config.conf
```

Ici :
- La racine du système est `/`
- Le dossier personnel de l’utilisateur est `/home/alice`

---

## 4. Chemins absolus et chemins relatifs

### 4.1 Chemin absolu

Un **chemin absolu** commence toujours par `/` et décrit le chemin complet depuis la racine.

Exemple :

```text
/home/alice/documents/cours.txt
```

Ce chemin est valide quel que soit le répertoire courant.

---

### 4.2 Chemin relatif

Un **chemin relatif** est exprimé par rapport au répertoire courant.

Si le répertoire courant est :

```text
/home/alice
```

Alors :

- Vers le fichier `cours.txt` :

```text
documents/cours.txt
```

- Depuis `/home/alice/images` vers `cours.txt` :

```text
../documents/cours.txt
```

(`..` signifie « remonter d’un niveau »)

---
!!! tip A RETENIR
    - Un **chemin absolu** commence par `/` et est indépendant du répertoire courant.
    - Un **chemin relatif** dépend de l’endroit où l’on se trouve. 

## 5. Exemples pratiques
```
/
├── home
│   └── alice
│       ├── documents
│       │   └── cours.txt
│       └── images
│           └── photo.jpg
└── etc
    └── config.conf
```

### Exemple 1 : se déplacer et lister


```bash
cd /home/alice
ls
affiche : documents  images
```

### Exemple 2 : afficher un fichier avec un chemin relatif

```bash
cd /home/alice
cat documents/cours.txt
```

### Exemple 3 : afficher le même fichier avec un chemin absolu

```bash
cat /home/alice/documents/cours.txt
```

### Exemple 4 : déplacer un fichier avec un chemin relatif 
Le répertoire courant est images
```bash
mv photo.jpg   ../documents/
```



