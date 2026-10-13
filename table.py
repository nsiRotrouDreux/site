def table(m) : #m est le motif à traiter
             d=[{} for i in range (len(m))]
             for j in range (len(m)):
                 for k in range(j):
                     d[j][m[k]]  = k
             return d 
print(table ('maman'))