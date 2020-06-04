# current algebra of gl(m|n) of stardard parity. May add some other current algebra of other parities later. 
# Compute the commutation relations. 
# compute the universal Bethe algebra.
import re

def de(i,j):# delta function, return 1 if i=j, 0 otherwise.
    return 1 if i == j else 0

def sgn(s,i,j,k,l):# given parity sequence s, and indices i, return the corresponding sign.
    return -1 if (s[int(i)] != s[int(j)]) and (s[int(k)] != s[int(l)]) else 1

def commutator(s,se): # replace a commutator in string s by its value. se is the parity sequence. 
    bra = re.compile(r'\[e(\d+)\,(\d+)\[(\d+)\]\,e(\d+)\,(\d+)\[(\d+)\]\]') # bracket of the form [ei,j[p],ek,l[q]], where ei,j[p] is the p-th node of ei,j.
    i,j,p,k,l,q = bra.findall(s)[0]
    return '{}*e{},{}[{}]-{}*e{},{}[{}]'.format(de(j,k),i,l,int(p)+int(q),de(i,l)*sgn(se,i,j,k,l),k,j,int(p)+int(q))