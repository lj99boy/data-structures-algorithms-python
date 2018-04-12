# while j<n and i<m:
#     if i == -1:
#         j,i= j +1,i+1
#     elif t[j] == p[i]:
#         j,i=j+1,i+1
#     else:
#         i = pnext[i]

def matching_KMP(t,p,pnext):
    j,i = 0,0
    n,m = len(t),len(p)
    while j<n and i<m:
        if i == -1 or t[j]==p[i]:
            i,j = (i+1,j+1)
        else:
            i = pnext[i]
    if i==m:
        return j-i
    else :
        return -1


def gen_pnext(p):
    i,k,m = 0,-1,len(p)
    pnext = [-1] * m
    while i < m-1:
        if k == -1 or p[i] == p[k]:
            i,k = (i+1,k+1)
            pnext[i] = k
        else:
            k = pnext[k]
    return pnext

print(gen_pnext('abbcabcaabbcaa'))
