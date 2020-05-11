# Currently only consider Y(gl(m|n)) case. Yangian of other types will be added later. 
# Currently only consider the standard parity case. Other cases will be added later.
import re
from itertools import permutations
def bilinear_form(x,y,s): # x,y are basis vectors of weight space, s is the parity sequence. # Basis vectors are in the form 'ei'.
    if x == y:
        m = re.search(r'(?<=e)\d+',x) # find i in 'ei'.
        return s[int(m.group(0))] # value of si.
    else:
        return 0

def qdet(m): # m is a matrix with noncommutative entries. qdet is the collumn determinant.
    l = len(m)
    qdet = ''
    for i in permutations:
        term = ''
        for j in range(len(m)-1):
            term = term + (m[i[j]][j])+'*'
        term = term + '*' + (m[i[len(m)-1]][len(m)-1])
        qdet =  '+' + term
    return qdet