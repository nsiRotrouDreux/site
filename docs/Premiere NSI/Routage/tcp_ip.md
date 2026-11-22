# Cours : protocoles et modèle TCP/IP (NSI Première)

## 1. Les protocoles DNS, DHCP, TCP et IP

Un **protocole** est un ensemble de règles qui définissent comment deux machines échangent des données (format des messages, ordre des échanges, réactions en cas d'erreur). Sans protocole commun, deux ordinateurs ne pourraient pas se comprendre.

**IP (Internet Protocol).** Il s'occupe de l'adressage et de l'acheminement des données d'une machine à une autre à travers les réseaux. Chaque machine possède une **adresse IP** (par exemple `192.168.1.12` en IPv4, codée sur 32 bits). Les données sont découpées en **paquets** qui sont routés de proche en proche par les routeurs. IP ne garantit ni l'arrivée des paquets, ni leur ordre : on dit qu'il fonctionne en « *best effort* ».

**TCP (Transmission Control Protocol).** Il assure un transport **fiable** des données entre deux applications. Avant d'échanger, les deux machines établissent une connexion (la « poignée de main en trois temps » : SYN, SYN-ACK, ACK). TCP découpe les données en **segments**, les numérote, vérifie leur bonne réception grâce aux accusés de réception (ACK) et redemande les segments perdus. Il utilise des **ports** pour distinguer les applications (80 pour HTTP, 443 pour HTTPS, par exemple).

**DNS (Domain Name System).** C'est l'« annuaire » d'Internet : il traduit un nom de domaine lisible (`www.education.gouv.fr`) en adresse IP, car les machines communiquent avec des adresses et non avec des noms. Quand on saisit une adresse dans un navigateur, une requête est envoyée à un **serveur DNS** qui répond avec l'adresse IP correspondante.

**DHCP (Dynamic Host Configuration Protocol).** Il permet à une machine qui se connecte à un réseau de recevoir **automatiquement** sa configuration : adresse IP, masque de sous-réseau, passerelle par défaut (le routeur) et adresse du serveur DNS. Sur un réseau domestique, c'est la box qui joue le rôle de serveur DHCP. Cela évite de configurer chaque appareil à la main.

**Exemple de scénario complet :** un ordinateur se connecte au Wi-Fi (DHCP lui donne une adresse IP), l'utilisateur tape un nom de site (DNS donne l'adresse IP du serveur), puis le navigateur ouvre une connexion (TCP) et les données circulent sous forme de paquets (IP).

## 2. Le modèle TCP/IP

Le modèle TCP/IP décrit l'organisation de la communication réseau en **couches**. Chaque couche a un rôle précis, rend un service à la couche supérieure et s'appuie sur la couche inférieure.

### Schéma des couches

```
 ÉMETTEUR                                                    RÉCEPTEUR

┌─────────────────────────┐                      ┌─────────────────────────┐
│  4. APPLICATION         │  ← message →         │  4. APPLICATION         │
│  HTTP, DNS, DHCP, SMTP  │                      │  HTTP, DNS, DHCP, SMTP  │
├─────────────────────────┤                      ├─────────────────────────┤
│  3. TRANSPORT           │  ← segment →         │  3. TRANSPORT           │
│  TCP, UDP  (ports)      │                      │  TCP, UDP  (ports)      │
├─────────────────────────┤                      ├─────────────────────────┤
│  2. INTERNET            │  ← paquet →          │  2. INTERNET            │
│  IP  (adresses IP)      │                      │  IP  (adresses IP)      │
├─────────────────────────┤                      ├─────────────────────────┤
│  1. ACCÈS RÉSEAU        │  ← trame →           │  1. ACCÈS RÉSEAU        │
│  Ethernet, Wi-Fi (MAC)  │                      │  Ethernet, Wi-Fi (MAC)  │
└────────────┬────────────┘                      └────────────┬────────────┘
             │                                                │
             └──────────── support physique ──────────────────┘
                      (câble, Wi-Fi, fibre...)

   ENCAPSULATION ↓  (à l'envoi)            DÉSENCAPSULATION ↑  (à la réception)
```

### Les quatre couches

| Couche | Rôle | Exemples de protocoles | Unité de données |
|---|---|---|---|
| **Application** | Fournit les services aux logiciels de l'utilisateur | HTTP, HTTPS, DNS, DHCP, SMTP, FTP | Message / donnée |
| **Transport** | Communication de bout en bout entre applications (ports, fiabilité) | TCP, UDP | **Segment** (TCP) ou datagramme (UDP) |
| **Internet (réseau)** | Adressage et routage entre réseaux | IP, ICMP | **Paquet** |
| **Accès réseau** | Transmission physique sur le support local (câble, Wi-Fi) | Ethernet, Wi-Fi | **Trame** |

### Segment, paquet, trame

Lorsqu'une donnée descend les couches côté émetteur, chaque couche lui ajoute un **en-tête** contenant ses propres informations : c'est l'**encapsulation**.

- **Segment** (couche transport) : la donnée de l'application est découpée, et TCP ajoute un en-tête contenant notamment les **ports source et destination**, le **numéro de séquence** et le numéro d'acquittement.
- **Paquet** (couche Internet) : le segment est placé dans un paquet auquel IP ajoute un en-tête contenant les **adresses IP source et destination**.
- **Trame** (couche accès réseau) : le paquet est placé dans une trame à laquelle Ethernet ou Wi-Fi ajoute un en-tête avec les **adresses MAC** (adresses physiques des cartes réseau) de la machine suivante, ainsi qu'une séquence de contrôle d'erreur en fin de trame.

```
Donnée  →  [En-tête TCP | Donnée]  →  [En-tête IP | En-tête TCP | Donnée]  →  [En-tête Ethernet | En-tête IP | En-tête TCP | Donnée | Contrôle]
            SEGMENT                    PAQUET                                   TRAME
```

Côté récepteur, le chemin inverse s'effectue : c'est la **désencapsulation**. Chaque couche lit et retire son en-tête avant de transmettre le contenu à la couche supérieure.

### À retenir

- Les routeurs travaillent principalement au niveau **IP** (paquets) : ils lisent l'adresse IP de destination pour choisir le prochain chemin.
- Les adresses IP identifient une machine sur un **réseau mondial**, les adresses MAC identifient une carte réseau sur un **réseau local**. L'adresse MAC est réécrite à chaque saut, pas l'adresse IP.
- Les ports identifient une **application** sur une machine.

## Exercices d'application

1. Quel protocole traduit `www.exemple.fr` en adresse IP ? Quel protocole fournit son adresse IP à un ordinateur qui vient de se connecter au réseau ?
2. Citer deux différences entre TCP et IP.
3. Dans quel ordre les en-têtes sont-ils ajoutés à une donnée lors de l'envoi ? Nommer l'unité de données obtenue à chaque étape.
4. Un routeur lit-il l'adresse MAC ou l'adresse IP de destination pour décider où envoyer un paquet ?
