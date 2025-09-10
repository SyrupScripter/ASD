from egz3atesty import runtests
import heapq
'''
idea:
mam kolejke prior.
ide po posortowanych przedziałach po x[0],x[1]; sprawdzam, początek przedziału 
i usuwam wszystkie które są za początkiem tego

dodaje do kolejki, rozpatrywany przedział

w taki sposób, patrze ile w danym momencie mam 'odpadów' w kolejce i wiem,
że w miejscu rozpatrywanym jest ileś

żeby nie sprawdzać za każdym razem całej kolejki, to używam heapq, które pozwala mi
znaleźć najmniejszy element w O(1), dodawanie do kolejki w log(n), łącznie O(nlog(n))

time complexity - O(nlogn)
space complexity - O(n)
'''

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    I.sort()

    q = []
    biggie = 0
    for interval in I:
        s = interval[0]

        if(interval[0]==interval[1]):   # ponieważ są domknięte przedziały, musimy to rozpatrywać, inaczej możemy pominąć rozw
            biggie = max(biggie, len(q)+1)
        else:
            biggie = max(biggie, len(q))

        while(len(q)>0):
            if(s>q[0]):
                heapq.heappop(q)
            else:
                break
        
        heapq.heappush(q, interval[1])
    

    return biggie

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
