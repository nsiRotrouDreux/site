def decalage(d, j,c):
    if c in d[j]:
        return j-d[j][c]  # il y a une clé 'c'à l'indice j
    else:
        return j+1  # la lettre c n'est pas présente à gauche dans le motif, on se met en j+1