# Sécurisation des communications

## 1. Introduction

On a vu en première comment deux ordinateurs communiquaient à travers la relation client serveur . Une fois la connexion établie , les échanges de données se font à l’aide du protocole http.

Sur internet les communications se font en utilisant une série de protocoles , organisés en couche :


   	* Couche matérielle (ethernet, fibre…)
   	* Couche internet , avec le protocole IP
   	* Couche transport avec les protocoles UDP et TCP par exemple
   	* Couche d’application avec les protocoles de haut niveau comme http, Imap…

Les données transmises sont découpées en paquets qui transitent de routeurs en routeurs et peuvent donc être lues…Ce qui n’est pas top , notamment pour tout ce qui touche aux transactions bancaires.

On est donc amené à sécuriser les communications  avec plusieurs contraintes :

	* S’assurer que le client se connecte au bon serveur
	* S’assurer que le contenu d’une trame ne soit lisible que par la source et la destination.
    * Ne pas rendre la pocédure de chiffrage trop lourde afin de ne pas ralentir la communication.

Deux techniques principales ont émergé :

	* Le chifrement symétrique 
	* Le chiffrement asymétrique 

## 2. Le chiffrement symétrique 
Utiliser un chiffrement symétrique signifie coder et décoder avec une même clé .
Cela signifie qu’aux deux bouts de la chaine , la clé de codage et de décodage est connue et a la même valeur . C’est le cas lors de cryptage simple comme le codage Cesar ou le code de Vigenere.

**Exemple de codage en python du code Cesar :**
``` py 
 def code(mot, decalage):
    mot= mot.upper()
    decalage= decalage%26
    nv_mot = ''
    for lettre in mot :
        a = ord(lettre) +decalage
        if a>90       :
            a= a-26
            
        nv_mot += chr(a)
    return nv_mot
```
La fonction decodage va utiliser la même clé 
``` py
def decode(mot, decalage):
    mot= mot.upper()
    decalage= decalage%26
    nv_mot = ''
    for lettre in mot :
        a = ord(lettre) - decalage
        if a<65:
            a= a+26
            
        nv_mot += chr(a)
    return nv_mot
```