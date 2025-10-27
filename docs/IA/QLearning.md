# Présentation du Q‑Learning

## Introduction
Q‑Learning est un algorithme d'apprentissage par renforcement, sans modèle (model‑free) et hors‑politique (off‑policy), qui apprend une fonction de valeur d'action Q(s, a) pour maximiser la récompense cumulée.
On va ici, à travers un exemple, construire la table qui permet à l'algorithme de converger .

## Fonctionnement et mise à jour 
- L'idée est de mettre à jour une table qui va permettre de trouver le meilleur chemin pour arriver à la récompense .
Cette table est mise à jour à l'aide d'une formule mathématique que l'on verra plus loin. 
A chaque étape , l'agent choisi une action. Suite à cette action , on met à jour la valeur qui est associée au choix de l'agent.
La nouvelle valeur dépend:

* Du coefficient choisi (α)
* De la valeur de la case d'où l'agent arrive Q
* De la valeur associée à la case d'arrivée R
* De la valeur maximale de la case d'arrrivée  max(Q)

formule : Q = Q*(1-α) + α(R+(1-α)max(Q))

Exemple :


## Mise à jour (règle de Bellman itérée)
`Q(s,a) ← Q(s,a) + α * (r + γ * max_a' Q(s',a') - Q(s,a))`  
avec α = taux d'apprentissage, γ = facteur d'actualisation.

## Pseudo‑code (essentiel)
```text
Initialize Q(s,a) arbitrairement
pour chaque épisode:
    initialiser s
    tant que s non terminal:
        choisir a depuis s (ε‑greedy sur Q)
        exécuter a, observer r, s'
        Q(s,a) ← Q(s,a) + α*(r + γ*max_a'Q(s',a') - Q(s,a))
        s ← s'
```

## Particularités dans l'apprentissage par renforcement
- Off‑policy : apprend la valeur de la politique optimale indépendamment de la politique suivie pour explorer.
- Model‑free : pas besoin de connaître ou d'estimer la dynamique P(s'|s,a).
- Bootstrapping : mise à jour basée sur estimations courantes → converge sous conditions (taux d'apprentissage décroissant, visite fréquente de tous les couples (s,a)).
- Sensible à l'exploration : mauvaise exploration → mauvaise estimation des Q.
- Fonction d'approximation : pour grands espaces d'état/action, utiliser réseaux (DQN) modifie stabilité et exige techniques supplémentaires (replay buffer, target network).
- Efficacité échantillonnale généralement moindre que méthodes basées sur modèles.

## Hyperparamètres clés
- α (learning rate), γ (discount), ε (exploration), politique d'exploration et son décroissement, nombre d'épisodes/étapes, taille du buffer et batch (si apprentissage par lot).

## Avantages / Limites rapides
- Avantages : simple, convergent (pour tableaux finis), off‑policy.
- Limites : ne scale pas bien sans approximation, instable avec réseaux, nécessite beaucoup d'échantillons.

## Extensions courantes
- Deep Q‑Network (DQN), Double DQN, Dueling DQN, Prioritized Experience Replay, Q‑learning adaptatif.

## Références
- Sutton & Barto, "Reinforcement Learning: An Introduction" (chapitre sur Q‑learning).
- Articles sur DQN et ses variantes pour fonction d'approximation.
