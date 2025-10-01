from egz3atesty import runtests
from queue import Queue

'''
zlozonosc czasowa: E + V (BFS)

idea: rozszerzam grzyb zgodnie z kolejnością, każdy z kolejki
każde rozszerzenie wkładam na koniec kolejki i potem znowu rozszerzam każdy o 1

zliczam ile jest danego grzyba w visited
'''

def mykoryza( G,T,d ):
  # tu prosze wpisac wlasna implementacje
  q = Queue()
  n = len(G)

  visited = [-1 for _ in range(n)]

  for idx in range(len(T)):
    q.put((T[idx],idx))
    visited[T[idx]] = idx
  
  while(not q.empty()):
    skad,nr_grzyba = q.get()
    for dokad in G[skad]:
      if(visited[dokad] == -1): #nie zajety
        visited[dokad] = nr_grzyba
        q.put((dokad,nr_grzyba))

  ile=0
  for i in range(n):
    if(visited[i]==d):
      ile+=1


  return ile

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
