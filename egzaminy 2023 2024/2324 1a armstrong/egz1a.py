from egz1atesty import runtests
from queue import PriorityQueue

'''
dla każdego wierzchołka, znajdujemy odległość od startu i od końca (dijkstra)
następnie iterujemy przez wierzchołki, wybieramy najlepszy rower
obliczamy łączny dystans, do wierzchołka i od wierzchołka z rowerem do końca 
(to działa, ponieważ możemy wziąć max 1 rower)
'''

def dijkstra(B,G,n,s,t):
  q = PriorityQueue()
  q.put((0,s))
  dist = [float('inf') for _ in range(n)]
  dist[s]=0

  while(not q.empty()):
    laczny_dist_skad, skad = q.get()

    for dokad, koszt in G[skad]:
      #relaxation
      if(dist[dokad] > dist[skad] + koszt):
        dist[dokad] = dist[skad] + koszt
        q.put((dist[dokad],dokad))
  return dist

def armstrong( B, G, s, t):
  # tu prosze wpisac wlasna implementacje
  n=0
  for i,j,k in G:
    n = max(n,i,j)
  n+=1
    
  best_rower = [1 for _ in range(n)]  # w każdym wierzchołku, zapisuje najlepszy rower
  for i,p,q in B: # iteruje przez rowery - O(kilka * V)
    if(p<q):  # tylko patrzymy na rowery ktore pomagają
      best_rower[i] = min(best_rower[i],p/q)

  # lista sasiedzstwa
  sasiedzi = [[] for _ in range(n)]
  for i,j,k in G:
    sasiedzi[i].append((j,k))
    sasiedzi[j].append((i,k))

  dist1 = dijkstra(B,sasiedzi,n,s,t) # dystans od poczatku do kazdego
  dist2 = dijkstra(B,sasiedzi,n,t,s) # dystans od konca do kazdego

  min_dystans = float('inf')
  # inny sposób - prostszy, iteruje przez rowery i sprawdzam każdy, best_rower nie potrzebne
  # for nr,p,q in B:  #O(V*kilka)
  #   if(p<q):
  #     min_dystans = min(min_dystans, dist1[nr] + (p/q)*dist2[nr])
  for i in range(n): #O(V)
    min_dystans = min(min_dystans, dist1[i] + best_rower[i]*dist2[i])
  
  min_dystans = min(min_dystans, dist1[t])

  return int(min_dystans) if min_dystans != float('inf') else -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
