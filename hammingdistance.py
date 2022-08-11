# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
from dis import dis


def HammingDistance(p, q):
    # your code here
    arrp = p.split()
    arrq = q.split()
    lengthp = len(p)
    lengthq = len(q)
    i=0
    j=0
    dist = 0
    for i in range(lengthp):
           if p[i]!=q[i]:
                dist=dist+1
    print(dist)            
    return dist

HammingDistance('CTACAGCAATACGATCATATGCGGATCCGCAGTGGCCGGTAGACACACGT','CTACCCCGCTGCTCAATGACCGGGACTAAAGAGGCGAAGATTATGGTGTG' )