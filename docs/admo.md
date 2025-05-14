# Un exemple

!!! note "Voyons donc"
     test
        
    !!! success "Great it works"
          or should
!!!note "Le décalage et son dictionnaire "
    On va utiliser ce code pour établir la table de décalage . d est la table obtenue précédemment, c est le caractère obtenu à l'indice j du motif.
         
    !!!success  "Le code décalage"
         
        ``` py
         def decalage(d, j,c):
              if c in d[j]:
                 return j-d[j][c]  # il y a une clé 'c'à l'indice j
              else:
                 return j+1  # la lettre c n'est pas 
                    #présente à gauche dans le motif,
                     # on se met en j+1
 
  
        ```