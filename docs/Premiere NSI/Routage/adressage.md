# ADRESSAGE

## I. Adresse MAC

Lorsqu'un ordinateur vit sa propre vie, il n'a pas besoin d'être
identifié.

On va quand même lui donner un nom, au cas où il rencontrerait d'autres
ordinateurs : cela pourra toujours servir.

**Adresse MAC (Media Access Control)**\
Format : `xx:xx:xx:xx:xx:xx`

12 caractères hexadécimaux → 6 octets → adresse unique par appareil.

Pour afficher son adresse MAC : - **Windows** → `ipconfig /all` -
**Linux/Unix** → `ip addr show`

------------------------------------------------------------------------

## II. Adresse IP

Une adresse IP sert à identifier un appareil sur un réseau.

### a. Types d'adresses IP

-   **IPv4** : 4 octets → exemple `192.168.2.78`
-   **IPv6** : 16 octets → exemple
    `214f:1234:a4f5:14d5:ffff:0a5e:8c5a:6bca`

Structure d'une adresse : - **net ID** : identifiant du réseau\
- **host ID** : identifiant de la machine

Notation CIDR :

Exemple : `192.168.5.57/24` → Les 24 bits de poids le plus fort servent à identifier  le réseau.

Adresses réservées : - Adresse réseau → `192.168.5.0` - Broadcast →
`192.168.5.255`
Il reste alors 254 adresses disponbles pour accueillir des machines (appelées _hotes_)
------------------------------------------------------------------------

### b. Attribution d'une adresse IP

L'adresse IP est fournie par le protocole  **DHCP** lors du démarrage de la
machine.

------------------------------------------------------------------------

### c. Adresse IP publique

Adresse visible depuis Internet, généralement celle de la
**box/routeur**.

Les appareils d'un foyer n'ont pas leur propre adresse publique.

------------------------------------------------------------------------

### d. Adresse IP privée

Adresse utilisée uniquement en réseau local, non accessible depuis
l'extérieur.

Exemple : réseau privé `192.168.0.0/24`.

Le routeur possède alors : - une **adresse privée** pour le LAN - une
**adresse publique** pour communiquer sur Internet

Voici des extraits obtenus à partir des informations d'une livebox

| Réseau privée| Réseau public |
| ---| ---|
|![adresse privée](adresseLivebox.png)|![adresse publique ](adressePublique.png)|


------------------------------------------------------------------------

## III. Masque de sous-réseau

Exemple :

Adresse : `192.45.2.9/24`

Masque correspondant :

    255.255.255.0

Le /24 indique que les 24 bits de poids le plus forts servent à identifier le réseau. On met alors leur bit à 1. On met les bits qui servent à identifier les machines à 0 , ici les 8 derniers.

On obtient en notation binaire : 11111111.11111111.11111111.00000000 soit 255.255.255.0

Le masque permet de déterminer le sous-réseau par un **ET logique** avec
l'adresse IP.
![alt text](masque1.png)

Ce calcul nous donne l'adresse du sous réseau .Pour avoir la dernière adresse disponible dans ce sous réseau, il suffit de mettre les bits de la partie hôte à 1  dans le masque . 

on a donc :

   - Adresse sous réseau : 192.45.2.0
   - Dernière adresse : 192.45.2.255

------------------------------------------------------------------------

### Exercice
1. Déterminer l'adresse réseau de :    192.168.210.9/20 et la dernière adresse disponible sur ce réseau
2. Faire l'exercice ci dessous :


!!! note "Exercices "

    Notre FAI a mis à notre disposition cette plage d'adresses IP : 192.168.160.0/21.

    0. Combien a-t-on d'adresses disponibles ?


    On veut créer un sous réseau pour les élèves , ils sont 850 , un pour les profs , il y en a 100 et un pour l’administration , 12 . Diviser un réseau en sous réseaux , cela s'appelle du **subnetting**


    1.	Calculez la plage d’adresses diponibles
    2.	Combien de bits sont nécessaires pour pouvoir caser tous les élèves . En déduire la valeur du masque puis les adresses alloués aux élèves
    3.	Faire de même pour les professeurs et l’administration

??? success "Correction"
 
     :smile: Y a rien !