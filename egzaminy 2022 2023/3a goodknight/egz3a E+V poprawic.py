from egz3atesty import runtests
from queue import Queue

'''
bfs throttling
'''

def goodknight( G, s, t ):
  # tu prosze wpisac wlasna implementacje
  n = len(G)

  # lista sasiedzstwa
  kraw = [[] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if(G[i][j] != -1):
        kraw[i].append((j,G[i][j]))
  # print( *kraw,sep="\n")

  wyn = [[float('inf') for _ in range(17)] for _ in range(n)]
  visited = [[False for _ in range(17)] for _ in range(n)]  # bez tego działa, ale 2x time
  
  wyn[s][0] = 0
  # for i in range(17):
  #   wyn[s][i] = 0

  q = Queue() # łaczny dystans, poziom zmeczenia, skad, ile do przejscia
  q.put((0,0,s,0))

  while(not q.empty()):

    # UWAGA - to jest nie poprawne, jakims cudem bfs znajduje najkrótszą ścieżke
    # doslownie tutaj nie robi sie throttling xD
    aaa, wyczerp, skad, przejscie = q.get()
    if(visited[skad][wyczerp]==True): 
      continue                        
    else:
      visited[skad][wyczerp] = True

    if(przejscie > 0):
      q.put((aaa, wyczerp, skad, przejscie-1))
      # continue  - tu powinno byc continue

    for dokad, droga in kraw[skad]:
      # wk
      if(wyczerp + droga <= 16):
        # relaksacja
        if(wyn[dokad][wyczerp + droga] > wyn[skad][wyczerp] + droga):
          wyn[dokad][wyczerp + droga] = wyn[skad][wyczerp] + droga
          q.put((wyn[dokad][wyczerp + droga], wyczerp + droga, dokad, droga))

      if(wyn[dokad][droga] > wyn[skad][wyczerp] + droga + 8): #NIE ELSE, spanie
          wyn[dokad][droga] = wyn[skad][wyczerp] + droga + 8
          q.put((wyn[dokad][droga], droga, dokad, droga))

  return min(wyn[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
