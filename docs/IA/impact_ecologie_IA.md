# Impact Écologique de l'Intelligence Artificielle

## Présentation du problème



## 1. Introduction
L’intelligence artificielle (IA) apporte de nombreux avantages, mais son développement et son utilisation ont un **coût environnemental** non négligeable. Celui-ci provient principalement de la consommation énergétique des centres de données, de l’entraînement des modèles, et de la fabrication du matériel.

---

## 2. Sources principales d’impact

### ⚡ Entraînement des modèles
- Les modèles de grande taille (LLM, vision, etc.) exigent des **millions à milliards de paramètres**.
- L’entraînement nécessite des **centaines à milliers de GPU** fonctionnant pendant des jours ou des semaines.
- Production notable de **CO₂**, parfois comparable à plusieurs années d’émissions d’un individu.

### 🖥️ Centres de données
- Consomment une forte quantité d’électricité pour :
  - le calcul,
  - le refroidissement,
  - l’alimentation continue.
- La demande énergétique des data centers augmente avec l’usage accru de l’IA.

### ⚙️ Fabrication du matériel (GPU, serveurs)
- Extraction de métaux rares et terres rares.
- Impact lié à la production industrielle.
- Durée de vie des composants souvent courte à cause de l’évolution rapide des architectures IA.

---

## 3. Impacts indirects
- **Eau** : certains centres utilisent d’importantes quantités d’eau pour le refroidissement.
- **Déchets électroniques** : hausse du renouvellement du matériel.
- **Infrastructure réseau** : le trafic numérique croît avec l’usage généralisé de l’IA.

---
## 4. Chiffres clés 2024 pour l’IA / data centers

En 2024, l’ensemble des data centers (cloud, calcul, stockage — dont une part importante liée à l’IA) a consommé ≈ 415 térawattheures (TWh) d’électricité dans le monde. 


Cela représente environ 1,5 % de la consommation électrique mondiale totale. 
Connaissance des Énergies


Dans un pays comme les États-Unis, les data centers consomment à eux seuls — en 2024 — ≈ 183 TWh, ce qui représente plus de 4 % de la consommation électrique nationale. 


On note aussi que la consommation des data centers a cru fortement ces dernières années — en grande partie à cause de l’essor de l’IA. 


:warning: Ces chiffres concernent tous les data centers — on ne peut pas attribuer avec précision toute cette consommation à l’IA seule (certains datacenters font du stockage, hébergement de sites, cloud, calcul non-IA…). Mais l’essor de l’IA rend la tendance à la hausse plus probable.


La consommation des data centers mondiaux (415 TWh/an) est — selon un des rapports récents — équivalente à la consommation électrique annuelle d’un pays comme la France


## 6. Ressources complémentaires
- Rapports sur l’empreinte carbone du numérique.
- Études sur les data centers et la consommation énergétique.
- Pistes de recherche en IA durable (Green AI, Efficient ML).



------------------------------------------------------
# 📘 Fiche : Impact Écologique des Data Centers & de l’Intelligence Artificielle  
### (Énergie, Eau, Émissions & Tendances 2000–2024)

---

## 🔎 1. Contexte général

Les data centers constituent l’infrastructure physique essentielle au numérique contemporain — cloud, stockage, services web et surtout **entraînement/exécution des modèles d’IA**.  
Leur impact environnemental croît rapidement, notamment du fait de :

- la demande en calcul (GPU/TPU) pour l’IA,
- la prolifération des services cloud,
- l’augmentation du volume des données,
- la densification du matériel.

---

## ⚡ 2. Consommation d’énergie (électricité)

### 🔢 Chiffres clés 2024
- **≈ 415 TWh/an** : consommation électrique mondiale des data centers en 2024.  
- Équivalent : **≈ la consommation annuelle d’un pays comme la France**.  
- Poids global : **1,5 % de la consommation électrique mondiale**.  
- Aux États-Unis : **≈ 183 TWh/an**, soit >4 % de la consommation du pays.

### 🔄 Évolution 2000 → 2024 (tendance indicative)
| Année | Consommation estimée | Commentaire |
|-------|-----------------------|-------------|
| 2000  | ~120 TWh/an          | Début du cloud, faible densité |
| 2010  | ~200 TWh/an          | Explosion web, streaming |
| 2020  | ~330 TWh/an          | Big data, cloud hyperscale |
| 2024  | ~415 TWh/an          | Montée IA + GPU intensifs |

> La croissance est exponentielle depuis 20 ans, malgré des gains d’efficacité (PUE).

---

## 💧 3. Consommation d’eau (refroidissement)

### 🔢 Chiffres clés
- Un data center peut consommer **jusqu’à 416 000 m³/an**.  
- Les plus grands « hyperscale » peuvent employer **≈ 22 000 m³ /jour**  
   
  C'est l'équivalent à la consommation d’une **petite ville (10–50k habitants)**.
- [WUE](<https://pue.webaxys.net/wue.html>) (Water Usage Effectiveness) moyenne : **≈ 1,8–2 L/kWh**.

### 🌡️ Pourquoi autant d’eau ?
- Refroidissement évaporatif (les plus gourmands en eau).  
- Maintien de température stable pour les GPU/CPU.  
- Climats chauds = consommation encore plus élevée.

### 📉 Évolution qualitative 2000 → 2024
| Année | Eau utilisée (estimation globale) | Tendance |
|-------|-----------------------------------|----------|
| 2000  | ~150 millions m³/an              | Premiers grands data centers |
| 2010  | ~220 millions m³/an              | Montée du cloud |
| 2020  | ~320 millions m³/an              | Explosion du streaming + IA |
| 2024  | ~400 millions m³/an              | Hyperscale + entraînement IA |

⚠️ L’historique exact est difficile à établir :  
- peu de reporting avant 2015,  
- technologies de refroidissement très variées,  
- absence d’obligation de transparence.

---

## 🌍 4. Émissions de CO₂ (électricité + refroidissement)

### Chiffres clés 2024
- **≈ 180 Mt CO₂/an** liés à l’électricité des data centers.  
- Forte variabilité selon le **mix énergétique local**.

---

## 📈 5. Scénarios d’évolution (2030–2035)

| Période | Énergie | Émissions CO₂ | Notes |
|---|---|---|---|
| **2024 (réf.)** | 415 TWh | 180 Mt | situation actuelle |
| **2030 – Base Case** | ~945 TWh | ~300 Mt | demande IA modérée |
| **2035 – Croissance IA rapide** | ~1 700 TWh | ~500 Mt | mix fossile + explosion IA |

---

## 🧠 6. Facteurs clés de l’impact IA

### ▪ Calcul intensif (GPU/TPU)
- Accélérateurs consommant **300–700 W par unité**.  
- Clusters IA = **plusieurs MW** continus.

### ▪ Explosion des données
- Stockage comptant pour **10–20 %** de la consommation des DC.

### ▪ Refroidissement
- Peut représenter **jusqu’à 40 %** de la consommation totale.

### ▪ Fabrication du matériel
- Impacts souvent ignorés dans les bilans carbone.  
- Métaux critiques : cuivre, cobalt, terres rares, aluminium.

---

## 📉 7. Tendances & améliorations possibles

### Déjà en déploiement :
- Free cooling (air extérieur).  
- Refroidissement liquide ou immersion.  
- Boucles fermées réduisant le prélèvement d’eau.  
- IA pour optimiser la gestion énergétique.
[Pour aller plus loin](https://www.weeedoit.com/les-technologies-de-refroidissement-pour-les-data-centers)

### Limites actuelles :
- Le besoin en calcul augmente **plus vite** que les gains d’efficacité.  
- Les zones chaudes / sèches subissent une pression hydrique.  
- Concentration géographique → vulnérabilité environnementale locale.

---
## 8. Consommation de Chat GPT 3

Le PUE  indique quel est le ratio entre l'énergie totale consommée par l'ensemble du centre d'exploitation (avec entre autres, le refroidissement, le traitement d'air, les UPS (onduleurs)...) et la partie qui est effectivement consommée par les systèmes informatiques que ce centre exploite (serveurs, stockage, réseau)  _source wikipedia_
![alt text](image.png)

[Pour aller plus loin]( https://generationia.flint.media/p/comment-calculer-vraiment-impact-carbone-de-chatgpt-climat-ia-eau)

## 🧭 8. Conclusion

Les data centers et l’IA ont une empreinte écologique croissante, tant en énergie qu’en eau.  
Même si des progrès technologiques existent, la **demande en calcul IA augmente plus vite que l’efficacité**, ce qui risque de renforcer :

- la consommation électrique,  
- les besoins en eau,  
- les émissions de CO₂,  
- la pression sur les territoires.

Une stratégie durable nécessite :
- une transition massive vers les **renouvelables**,  
- l’optimisation du refroidissement,  
- une transparence accrue sur l’eau et l’énergie,  
- des choix de conception IA plus sobres.

---


