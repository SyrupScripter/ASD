#find the k-smallest element asap
from random import randint
def partition(T,p,q):
    i = p
    for j in range(p,q):
        if(T[j]<=T[q]):
            T[j],T[i]=T[i],T[j]
            i+=1
        
    T[q],T[i]=T[i],T[q]
    
    return i

def quickselect(T,p,q,k):
    if(p<=q):
        if(p==q):
            return T[p]
        
        piv = partition(T,p,q)

        if(piv==k):
            return T[piv]
        elif(k>piv):
            #print("1")
            return quickselect(T,piv+1,q,k)
        else:
            #print("2")
            return quickselect(T,p,piv-1,k)
            

#testy
for _ in range(20):
    k = randint(0, 9)
    a = [randint(10, 99) for _ in range(10)]
    expected = sorted(a)[k]

    result = quickselect(a, 0, len(a) - 1, k)

    assert expected == result
    print(a, expected, "num:", k, "ok")



#T = [1,2,9,2,8,4]
#print(partition(T,0,len(T)-1))
#print(T)

#print(quickselect(T,0,len(T)-1,0))