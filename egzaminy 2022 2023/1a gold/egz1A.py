from egz1Atesty import runtests
from queue import PriorityQueue

'''
time complexity - O(ElogV) = O(V^2logV)

Aby znaleźć najlepszą drogę, możemy:
- puścić algortym dijsktry, od początku, aby znaleźć najkrótszą drogę do każdego zamku przed rabunkiem
- puścić algortym dijkstry, od końca, aby znaleźć najktórszą drogę do każdego zamku po rabunku
(zliczamy krawędzie, jak po rabunku)
- dla każdego wierzchołka, sprawdzamy dystans przed rabunkiem + dystans po rabunku - ilość złota w zamku
'''

def dijsktra(G,s,t,r=0,mn=1):
  n = len(G)
  q = PriorityQueue()
  q.put((0,s))

  best_dist = [float('inf') for _ in range(n)]
  best_dist[s] = 0

  while(not q.empty()):
    obecny_dist,skad = q.get()

    if(best_dist[skad] != obecny_dist):
      continue 

    for dokad, distance in G[skad]:
      #relaxation
      if(best_dist[dokad] > best_dist[skad] + distance*mn + r):
        best_dist[dokad] = best_dist[skad] + distance*mn + r
        q.put((best_dist[dokad],dokad))
  
  return best_dist

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n = len(G)

  before_steal = dijsktra(G,s,t)
  after_steal = dijsktra(G,t,s,r,2)

  # print(before_steal)
  mini = float('inf')
  for vault in range(n):
    mini = min(mini, before_steal[vault] + after_steal[vault] - V[vault])

  return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
