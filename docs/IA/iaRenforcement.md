## Définition de l'apprentissage par renforcement

L’apprentissage par renforcement ((Reinforcement Learning, RL)) est une technique utilisée en intelligence artificielle, où un agent (par exemple, un robot ou un logiciel) apprend à prendre les meilleures décisions en interagissant avec son environnement. À chaque action qu’il effectue, il reçoit une récompense (positive ou négative), et au fil du temps, il tente de maximiser la somme de ces récompenses. On parle souvent de méthode essai-erreur, car l’agent expérimente différentes stratégies, corrige ses erreurs et améliore ses choix progressivement.



L'agent n'est pas explicitement programmé pour accomplir une tâche, mais il découvre par essais et erreurs quelles actions mènent aux meilleurs résultats.

---

## Exemples simples de fonctionnement

### 1. Labyrinthe

Supposons un robot qui doit traverser une pièce remplie d’obstacles pour atteindre une sortie. À chaque mouvement, il peut recevoir :

+10 s’il se rapproche de la sortie

-5 s’il heurte un obstacle
Au début, le robot agit un peu au hasard. À force d’essais, il apprend à éviter les obstacles et à trouver le chemin le plus rapide vers la sortie, car les récompenses lui indiquent ce qui est bénéfique ou non. Et vive les tondeuses qui tondent toutes seules !




### 2. Robot ramasseur d'objets

Un robot doit ramasser des objets dans une pièce :
- +5 points pour chaque objet ramassé,
- -2 points s'il heurte un obstacle.

Le robot apprend à naviguer efficacement pour maximiser les objets collectés.

---

L'apprentissage par renforcement est utilisé dans de nombreux domaines comme les jeux vidéo, la robotique, et l'optimisation de processus.


## Deep Blue et AlphaZero pour comprendre la différence de fonctionnement

### Deep Blue

Deep Blue est le nom de la machine qui fit sensation en 1997, battant le champion du monde G. Kasparov aux échecs. Pour autant, cette machine n'a pas été formée avec du renforcement mais préformatée par des humains .

Son approche reposait principalement sur des techniques de calcul intensif : il évaluait des millions de positions à chaque coup grâce à des algorithmes de recherche (Minimax) et une vaste base de données de parties d’échecs humaines. En informatique  on parle de **Force Brute** .
Deep Blue n’apprenait donc pas par essai-erreur en recevant des « récompenses » comme c’est le cas pour l’apprentissage par renforcement. 

### AlphaZero

AlphaZero est une intelligence artificielle conçue par DeepMind (Google) qui s’est illustrée en maîtrisant à un niveau surhumain les jeux d’échecs, de go et de shogi. Contrairement aux anciennes nmachines qui jouaient aux échecs  (comme  Deep Blue), AlphaZero n’utilise pas une base de données de parties humaines : il ne connaît que les règles du jeu et apprend tout seul, « à partir de zéro" : On a ici un exemple d'utilisation de l'apprentissage par renforcement.


## Le jeu du Nim

[Activité capytale](<capytale2.ac-paris.fr/p/basthon/n/?kernel=python3-legacy&mode=create&id=6934989>)




### Le processus en détail
!!! note "Le processus d'apprentissage en détail"

     Explorer le jeu de Nim avec 8 bâtonnets par apprentissage

     Prenons l’exemple du jeu de Nim avec 8 bâtonnets posés sur la table. Deux joueurs (ici : la "machine" et un humain) jouent à tour de rôle. À chaque tour, on peut retirer 1 ou 2 bâtonnets. Celui qui prend le dernier bâtonnet gagne.

     Imaginons que l’on veuille entraîner une machine avec apprentissage par renforcement à bien jouer.

     1. États possibles
     Chaque "état" correspond au nombre de bâtonnets restants (8 à 0).

     2. Actions possibles à chaque état

        Retirer 1 bâtonnet

        Retirer 2 bâtonnets

     3. Départ

         La machine commence. 
         
         
         Par exemple, il y a 8 bâtonnets :

         Si elle prend 1, il en reste 7.

         Si elle prend 2, il en reste 6.

     4. Récompense
           +1 si la machine gagne (prend le dernier bâtonnet)

           -1 si la machine perd

           0 autrement


    5. Processus d’apprentissage

         Au début, la machine choisit ses coups au hasard.

         À chaque partie, elle mémorise quelle action, dans quel état, lui a valu une victoire (ou une défaite).

        Au fil du temps, elle favorise les choix qui l’ont amenée à gagner et évite ceux qui l’ont fait perdre. C’est comme ajuster les "poids" du réseau : elle attribue des scores plus élevés aux actions qui marchent !

      Exemple chiffré (simplifié)
      Imaginons :

      La machine joue et il reste 8 bâtonnets.

      Dans sa mémoire, elle a noté :

      En enlevant 1 bâtonnet à 8, elle a gagné 2 fois / perdu 3 fois (score = -1)

      En enlevant 2 bâtonnets à 8, elle a gagné 5 fois / perdu 1 fois (score = +4)

      Lorsqu’elle retrouve l’état "8 bâtonnets", elle va choisir l’action qui a le meilleur score : enlever 2 bâtonnets.

      Après de nombreuses parties et ajustements, elle adopte la meilleure stratégie (toujours favoriser les actions les plus récompensées). C’est exactement ainsi que l’apprentissage par renforcement fonctionne dans ce contexte : par l’expérience, la machine "tire leçon de ses erreurs" et affine ses choix pour gagner de plus en plus souvent.