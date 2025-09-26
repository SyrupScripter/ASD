from egz3atesty import runtests
from queue import PriorityQueue

'''
dijsktra ze stanem paliwa

badam jak idzie dobrycerz przy uwzględnieniu stanu wyspania, 
bez tego mozemy dostać niby "lepszy" wynik ale z gorszym wyspaniem co powoduje niepoprawne rozwiazanie


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
  
  wyn[s][0] = 0
  # for i in range(17):
  #   wyn[s][i] = 0


  q = PriorityQueue() 
  q.put((0,0,s))

  while(not q.empty()):
    aaa, wyczerp, skad = q.get() # łaczny dystans, poziom zmeczenia, skad

    if(wyn[skad][wyczerp] < aaa): # jak juz mamy lepszy wynik
      continue


    for dokad, droga in kraw[skad]:
      # wk
      if(wyczerp + droga <= 16):
        # relaksacja
        if(wyn[dokad][wyczerp + droga] > wyn[skad][wyczerp] + droga):
          wyn[dokad][wyczerp + droga] = wyn[skad][wyczerp] + droga
          q.put((wyn[dokad][wyczerp + droga], wyczerp + droga, dokad))

      if(wyn[dokad][droga] > wyn[skad][wyczerp] + droga + 8): #NIE ELSE, spanie
          wyn[dokad][droga] = wyn[skad][wyczerp] + droga + 8
          q.put((wyn[dokad][droga], droga, dokad))

  return min(wyn[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
