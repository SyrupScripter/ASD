from egz2btesty import runtests

'''
dijkstra z dodatkowym kosztem przy przesiadkach

'''
from queue import PriorityQueue

def tory_amos( E, A, B ): # mlogm
  # tu prosze wpisac wlasna implementacje
  l = len(E)
  n=0
  for i,j,dist,typ in E:  # wyznaczanie dlugosci tablicy
    n = max(n,i,j)
  n+=1

  # lista sasiedzstwa
  t = [[] for _ in range(n)]
  for i,j,dist,typ in E:
    t[i].append((j,dist,typ))
    t[j].append((i,dist,typ))

  best_distance = [[float('inf'),float('inf')] for _ in range(n)] # 0 - indyjska, 1 - p
  best_distance[A][0] = best_distance[A][1] = 0

  q = PriorityQueue()
  q.put((0,A,'n'))

  while(not q.empty()):
    aaa,skad,styp = q.get()
    if(skad == B):
      break
    for dokad,d,dtyp in t[skad]:
      if(dtyp == 'n'):
        continue
      elif(styp == "I" and dtyp == "I"):
        dodatek = 5
        if(best_distance[dokad][0]>best_distance[skad][0]+d+dodatek):
          best_distance[dokad][0] = best_distance[skad][0]+d+dodatek
          q.put((best_distance[dokad][0],dokad,dtyp))
      elif(styp == "P" and dtyp == "P"):
        dodatek = 10
        if(best_distance[dokad][1]>best_distance[skad][1]+d+dodatek):
          best_distance[dokad][1] = best_distance[skad][1]+d+dodatek
          q.put((best_distance[dokad][1],dokad,dtyp))
      elif(styp == 'n'):
        dodatek = 0 #??
        if(dtyp == "I" and best_distance[dokad][0]>best_distance[skad][0]+d+dodatek):
          best_distance[dokad][0] = best_distance[skad][0]+d+dodatek
          q.put((best_distance[dokad][0],dokad,dtyp))
        elif(dtyp == "P" and best_distance[dokad][1]>best_distance[skad][0]+d+dodatek):
          best_distance[dokad][1] = best_distance[skad][0]+d+dodatek
          q.put((best_distance[dokad][1],dokad,dtyp))
      else:
        dodatek = 20
        if(dtyp == "I" and best_distance[dokad][0]>best_distance[skad][1]+d+dodatek):
          best_distance[dokad][0] = best_distance[skad][1]+d+dodatek
          q.put((best_distance[dokad][0],dokad,dtyp))
        elif(dtyp == "P" and best_distance[dokad][1]>best_distance[skad][0]+d+dodatek):
          best_distance[dokad][1] = best_distance[skad][0]+d+dodatek
          q.put((best_distance[dokad][1],dokad,dtyp))


  return min(best_distance[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
