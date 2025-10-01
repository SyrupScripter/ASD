from egz3btesty import runtests
import heapq

'''
sortujemy przedziały, iterujemy przez posortowane przedziały, gdzie sprawdzamy czy rozpatrywany zachacza o inne
time complexity - O(nlogn), bo:
- słownik n
- sortowanie nlogn
- operacją while usuwam każdy element max 1 raz, wiec nie robi się n^2
- heappush max nlogn
'''

def uncool( P ):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    d = dict()
    for i in range(n):
        d.update({tuple(P[i]):i})

    P.sort()    #P.sort(key=lambda x: (x[0],x[1]))
    q = []
    for i in range(n):
        if(len(q)>0):
            elem = q[0]
            if(elem[1]>P[i][0] and elem[1]<P[i][1] and elem[0]<P[i][0]):
                # print(elem,P[i])
                return (d.get(tuple(elem)),d.get(tuple(P[i])))
            while(elem[1]<=P[i][0] and len(q)>0):
                heapq.heappop(q)
        heapq.heappush(q,P[i])

    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )


# def uncool( P ):
#   # tu prosze wpisac wlasna implementacje
#   n = len(P)
#   for i in range(n):
#     for j in range(i+1,n):
#       if(not(P[i][1]<P[j][0] or P[i][0]>P[j][1])):  # jak to nie spełnione to napewno sa osobno
#         if(P[i][0]<P[j][0] and P[i][1]>P[j][0] and P[i][1]<P[j][1]):
#           return (i,j)