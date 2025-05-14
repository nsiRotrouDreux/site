def table(m) : #m est le motif à traiter
    d=[{} for i in range (len(m))]
    for j in range (len(m)):
        for k in range(j):
            d[j][m[k]]  = k
    return d 

def decalage(d, j,c):
    if c in d[j]:
        return j-d[j][c]  # il y a une clé 'c'à l'indice j
    else:
        return j+1  # la lettre c n'est pas 
                    #présente à gauche dans le motif,
                     # on se met en j+1

def BM (motif, mot):
    d = table(motif)
    i = 0
    while i <= len(mot)-len(motif):
        k = 0
        for j in range (len(motif)-1 ,-1,-1):
            if mot[i+j] != motif[j]:
                k = decalage(d,j,mot[i+j])
                break
        if k  == 0 :
            print("l'indice",i," est solution")
            k = 1
        i += k

BM('gta','gtagatgtaggtaggtattagta')
