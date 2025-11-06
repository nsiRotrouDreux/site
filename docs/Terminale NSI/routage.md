# Cours — Routage, RIP, OSPF (avec rappel IPv4 et masque)



## Rappel — Adresse IPv4
- IPv4 = 32 bits, généralement écrit en notation décimale pointée : a.b.c.d (ex. 192.168.1.10).
- Chaque octet = 8 bits → valeurs 0–255.
- Adresse =partie réseau (à gauche)+ identifiant d’un hôte sur un réseau 

- Notation CIDR utilisé : Exemple 192.168.1.1 /24 signifie que les 24 premiers octects servent à coder l'adresse du réseau .

## Masque de sous‑réseau (CIDR)
- Masque = 32 bits indiquant la partie réseau : ex. /24 équivaut à 255.255.255.0.
- Notation CIDR : adresse/longueur (ex. 192.168.1.0/24).
- Calculs utiles :
    - Nombre d’adresses dans un préfixe /N = ${2}^{32−N}$.
    - Nombre d’hôtes utilisables ≈ ${2}^{32−N} − 2$ (réseau + broadcast) 
- Exemple : /26 → ${2}^{32−26}$ = 64 adresses, 62 hôtes utilisables, masque 255.255.255.192.

---

## Routage — principes
- But : faire transiter paquets d’un réseau source vers un réseau destination via routeurs.
- Table de routage : contient entrées (réseau de destination, masque, next hop/interface, métrique).
- Routage statique : administrateur configure manuellement. Simple mais peu scalable et non résilient.
- Routage dynamique : protocoles partagent informations et bâtissent tables automatiquement (RIP, OSPF, BGP, etc.).

---

## RIP (Routing Information Protocol)
- Famille : protocole vectoriel de distance.
- Versions : RIP v1 (classful), RIP v2 (classless, supports mask, auth).
- Métrique : nombre de sauts (hop count). Maximum = 15 (16 = inaccessible).

!!! info "Principes"

        Chaque routeur transmet à ses voisins les informations dont il dispose :
        Les adresses de ses propres voisins, les informations qu’il a déjà 
        reçues. Le routeur indique aussi la distance (en nombre de sauts) qui
         le sépare d’une machine donnée, soit combien de routeurs il faut
        traverser pour atteindre une machine en passant par lui. Le protocole RIP permet donc aux routeurs  
        d’échanger un couple (appelé vecteur de distance ) adresse distance


         Après une phase d’initialisation :
                • Un routeur peut découvrir une route vers un sous réseau inconnu : Il l’inscrit dans sa table.
        
                • Un routeur découvre une route plus courte vers un sous réseau déjà connu. Il efface
                  l’ancienne route et ajoute la route plus courte.
        
                • Un routeur reçoit une nouvelle route plus longue qu’un déjà connue. Il l’ignore
             
                • Un routeur reçoit une route existante mais plus longue vers un routeur passant par le même
                  voisin. Cela induit un problème sur le réseau. La table est mise à jour.
   
- Avantages : Simple à configurer, adapté aux petits réseaux.
- Limites :   Convergence lente, boucle possible, limite de 15 sauts, inefficace pour grands réseaux.


---

## OSPF (Open Shortest Path First)
- Famille : protocole à état des liens.
- Métrique : coût (généralement fonction inverse de la bande passante).         
    Formule généralement utilisée : $\frac{10^8}{débit}$ 

  | débit | coût |
  | -- | -- |
  |10 mbits| 10|
  |100 mbits| 1|
  |1 Gbits| 0.1|
  | 10 Gbits| 0.01|

!!! info "Principes "
    
    • Les routeurs sont répartis en zone et ne peuvent communiquer qu’avec les routeurs de leur zone, sauf un routeur de la zone , appelé ABR (Area Border Router).

    • Toutes les zones sont reliées à une zone centrale, la Zone 0, appelé BACKBONE.

    • La communication entre les différentes zones et la Backbone se fait par l’intermédiaire du routeur ABR.

    * Chaque routeur choisit une adresse unique parmi les adresses de son sous réseau.

    * Les routeurs envoient des messages à toutes les interfaces réseaux de leur zone. Ces messages contiennent l’identificateur du routeur, le numéro de zone et la liste des voisins qu’il connait déjà.

    * Quand un routeur reçoit ce type de message, il vérifie s’il connaît déjà l’expéditeur. Dans ce cas, il secontente d’envoyer un accusé de réception, validant le bon fonctionnement de la liaison. Dans le cas contraire, il transmet les informations dont il dispose. On parle de messages LSA ( Link state advertisement)

    *Après plusieurs échanges de messages, les routeurs d’une zone doivent avoir une vision complète de leur zone.

    * L’ensemble de cette première phase est appelé **diffusion ou inondation (flooding)**

    *Une fois que chaque routeur connaît la topologie de sa zone, il lui faut établir la meilleure route pour accéder à n’importe quel autre routeur de sa zone. Ceci fait, il inscrit ces données dans sa table de routage.

    *Le routeur ABR aura une autre spécificité. L’algorithme lui permettra de communiquer à toutes les autres zones, via la Backbone, les meilleures routes pour atteindre chaque sous réseau d’une zone

- Avantages :
    - Convergence rapide, meilleure échelle, routage optimisé selon coût, pas de limite artificielle de sauts.
- Complexité :
    - Plus de ressources CPU/mémoire, configuration plus avancée (areas, authentication, timers).

---

## Comparaison rapide RIP vs OSPF
- Type : RIP = distance‑vector ; OSPF = link‑state.
- Métrique : RIP = nombre de sauts ; OSPF = coût basé sur bande passante.
- Scalabilité : RIP limité ; OSPF adapté aux réseaux d’entreprise.
- Convergence : RIP lente ; OSPF rapide.
- Complexité : RIP simple ; OSPF plus complexe.

---




## Exemple — subdivision d’un /24 en /26

Réseau de départ : 192.168.1.0/24 (masque 255.255.255.0) — 256 adresses (254 hôtes utilisables).

Découpage en /26 (chaque /26 = 64 adresses, 62 hôtes utilisables) — on obtient 4 sous‑réseaux :

- 192.168.1.0/26  
    - Plage d’adresses : 192.168.1.0 — 192.168.1.63  
    - Réseau : 192.168.1.0  
    - Diffusion (broadcast) : 192.168.1.63  
    - Hôtes utilisables : 192.168.1.1 — 192.168.1.62 (62 adresses)

- 192.168.1.64/26  
    - Plage d’adresses : 192.168.1.64 — 192.168.1.127  
    - Réseau : 192.168.1.64  
    - Broadcast : 192.168.1.127  
    - Hôtes utilisables : 192.168.1.65 — 192.168.1.126

- 192.168.1.128/26  
    - Plage d’adresses : 192.168.1.128 — 192.168.1.191  
    - Réseau : 192.168.1.128  
    - Broadcast : 192.168.1.191  
    - Hôtes utilisables : 192.168.1.129 — 192.168.1.190

- 192.168.1.192/26  
    - Plage d’adresses : 192.168.1.192 — 192.168.1.255  
    - Réseau : 192.168.1.192  
    - Broadcast : 192.168.1.255  
    - Hôtes utilisables : 192.168.1.193 — 192.168.1.254
