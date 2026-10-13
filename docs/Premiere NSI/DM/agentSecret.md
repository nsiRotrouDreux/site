# Le décodeur de l'agent secret



## Scénario

Un agent secret reçoit des messages codés. Chaque message est une chaîne de caractères, et le code est **une combinaison de plusieurs techniques**. Ta mission : écrire les fonctions qui permettent de coder et de décoder ces messages.

**Règles du jeu**


- Teste chaque fonction avec les exemples donnés avant de passer à la suivante.
- Les messages ne contiennent que des lettres minuscules sans accent et des espaces.
- Tu peux utiliser les fonctions **ord** et **chr**

---

## Partie 1 : Échauffement

**1.** Écris une fonction `inverser(texte)` qui renvoie le texte écrit à l'envers.

```python
>>> inverser("espion")
'noipse'
```

**2.** Écris une fonction `compter_voyelles(texte)` qui renvoie le nombre de voyelles (a, e, i, o, u, y) du texte.

```python
>>> compter_voyelles("agent secret")
4
```

**3.** Écris une fonction `une_lettre_sur_deux(texte)` qui ne garde que les lettres situées aux positions paires (0, 2, 4...).

```python
>>> une_lettre_sur_deux("mission")
'msin'
```

---

## Partie 2 : Le chiffre de l'agent

Le code de l'agent fonctionne en **trois étapes** :

1. On supprime les espaces.
2. On remplace chaque lettre par la lettre qui la suit dans l'alphabet (`a` devient `b`, `b` devient `c`, ..., `z` devient `a`).
3. On insère le caractère `*` après chaque groupe de 3 lettres (mais pas à la fin du message).

**4.** Écris une fonction `supprimer_espaces(texte)`.

```python
>>> supprimer_espaces("rendez vous ce soir")
'rendezvouscesoir'
```

**5.** Écris une fonction `decaler(texte)` qui applique l'étape 2.

> *Indice :* utilise la chaîne `ALPHABET = "abcdefghijklmnopqrstuvwxyz"` et la méthode `ALPHABET.find(lettre)`, qui renvoie la position d'une lettre. Que se passe-t-il pour le `z` ?
 Pense à l'opérateur `%`. Ce n'est pas obligatoire .

```python
>>> decaler("abcxyz")
'bcdyza'
>>>ALPHABET.find('b')
1
```

**6.** Écris une fonction `inserer_etoiles(texte)`.

```python
>>> inserer_etoiles("abcdefgh")
'abc*def*gh'
>>> inserer_etoiles("abcdef")
'abc*def'
```

**7.** Écris une fonction `coder(message)` qui enchaîne les trois étapes.

```python
>>> coder("rendez vous ce soir")
'sfo*efa*wpv*tdf*tpj*s'
```

**8.** Écris une fonction `decoder(message_code)` qui fait le chemin inverse. Les espaces ne seront pas retrouvés, c'est normal.

```python
>>> decoder("sfo*efa*wpv*tdf*tpj*s")
'rendezvouscesoir'
```

> *Question de réflexion :* pourquoi ne peut-on pas retrouver les espaces ?

---

## Partie 3 : L'enquête

L'agent a intercepté ce message :

```python
mystere = "mfd*pmp*ofm*bus*bij*mbn*jtt*jpo"
```

**9.** Décode-le avec ta fonction `decoder`. Que dit le message ?

**10.** Un message est dit **suspect** s'il contient trois étoiles consécutives ou plus, **ou** s'il commence et finit par la même lettre. Écris une fonction `est_suspect(message)` qui renvoie `True` ou `False`.

```python
>>> est_suspect("abc***def")
True
>>> est_suspect("sfo*efa*wpv*tdf*tpj*s")
True
>>> est_suspect("mfd*pmp*of")
False
```

**11. (Défi)** Écris une fonction `mot_le_plus_long(phrase)` qui renvoie le plus long mot d'une phrase **sans utiliser `split`**.

> *Indice :* parcours la phrase caractère par caractère, construis le mot courant lettre après lettre, et garde en mémoire le meilleur mot trouvé jusqu'ici. Attention au dernier mot de la phrase !

```python
>>> mot_le_plus_long("le agent secret infiltre la base")
'infiltre'
```

---

## Pour aller plus loin

- **A.** Modifie `decaler` et `coder` pour ajouter un paramètre `pas` : `coder(message, 3)` décale de 3 lettres (chiffre de César).
- **B.** Écris une fonction qui affiche les 25 décodages possibles d'un message dont tu ne connais pas le décalage, pour le « casser ».