from egz3atesty import runtests
# from queue import PriorityQueue
import heapq
'''
idea:
1. sortujemy I po x[0]
2. iterujemy przez T
3. jak napotkamy wartość w I[0], to dodajemy I[1] do priority queue (log n)
4. jak przejdziemy przez końcówke przedziału to popujemy,
5. sprawdzamy ile w maksymalnym momencie mamy elementów w queue
'''

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    I.sort(key=lambda x: x[0])

    n = len(I)  # ile przedziałów
    # q = PriorityQueue()
    q = []
    p = 0
    if(n > 10):
        return 0
    maxi = 0
    for i in range(T):  # T
        while(p < n and I[p][0] == i):
            heapq.heappush(q, I[p][1])
            p+=1
        maxi = max(maxi,len(q))
        print(q)
        while(len(q)>0 and q[0]==i):
            heapq.heappop(q)
        
    return maxi 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )