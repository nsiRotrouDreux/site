## SPACE INVADERS
![alt text](spaceinvader.png)

Tu es prêt à coder ton premier jeu ? 

Un truc bien vintage , avec juste quelques couleurs, uet un module de python qui va te faciliter la tache , Pyxel.

### Débuter

Voici [le lien](<https://github.com/kitao/pyxel/blob/main/docs/README.fr.md>)   pour une documentation complète du module pyxel

On y retrouve par exemple les couleurs possibles ![alt text](couleur.png) et le numéro à utiliser pour les obtenir.

On va travailler en ligne sur le site https://www.pyxelstudio.net 

Une fois le site chargé:

 * Vous cliquez sur Create
 * Vous enregistrez  le lien qui vous est donné pour pouvoir retroucver votre travail
 * Vous allez coder dans la fenêtre de gauche , sous _import pyxel_
 * Et vous codez le jeu de space invaders :grin:
### Le début du jeu: Fixer la fenêtre et dessiner un vaisseau.

 Il y a dans notre progamme deux fonctions très importantes : draw et update ...la première dessine et la seconde met à jour .

 Donc , on fixe notre cadre, on place notre vaisseau dans le cadre en le dessinant (hyper basiquement, ne revez pas ! ), on le fait bouger et ...c'est déjà pas mal !

 Voici l'exemple 1 donné par la documentation: 

```py
import pyxel

pyxel.init(160, 120)      # on crée une fenêtre de 160 par 120

def update():
    if pyxel.btnp(pyxel.KEY_Q):   # appuyer sur la touche Q fait quitter 
        pyxel.quit()

def draw():
    pyxel.cls(0)   # on efface
    pyxel.rect(10, 10, 20, 20, 11) # on dessine un rectangle de coté 10 et 20, couleur 11 soit vert clair.

pyxel.run(update, draw) # on met à jour , on dessine .

```

A l'aide cet exemple :

* Créer une fenêtre carrée de 128 de coté
* Créer deux variables vaisseau_x et vaisseau_y et leur affecter à chacune une abscisse et une ordonnée (entre 0 et 128 :grin:)
* Créer une fonction deplacement_vaisseau donc voici la documentation

```py
def deplacement_vaisseau (x,y):
    """ Cette fonction permet de dpélacer la position du vaisseau:
    On utilisera la touche gauche (KEY_LEFT) pour aller vers la gauche, et les touches KEY_RIGHT, KEY_UP,KEY_DOWN pour les autres déplacements.
    On utilisera btn au lieu de btnp de l'exemple
    ATTENTION : l'origine du repère est en haut à gauche (coordonnées (0,0))
    entrée : Les coordonnées du vaisseau avant le mouvement
    sortie : les coordonnées du vaisseau après le déplacement
    """
    pass

```
* Compléter la fonction update() ci dessous

```py


def update():
    """ cette fonction met à jour les coordonnées du vaisseau
    """
     global vaisseau_x, vaisseau_y
     pass
```
* Compléter la fonction draw()

```py

def draw():
    """ Cette fonction  efface l'ecran et dessine un vaisseau carre de coté entre 7 et 9 , à votre choix . Vous avez le choix de la couleur
    """
    pyxel.cls(0)
    pyxel.rect(......)

pyxel.run(update, draw)
```