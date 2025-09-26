from egz2atesty import runtests

'''
Idea:
Licze sumy prefiksowe, po x i po y, od tyłu - ile jest pkt w danej współrzędnej

przy liczeniu x, sprawdzam, jaki jest maksymalny y dla danego x, ponieważ
nie mam co rozpatrywać dla danego x, punktu niższego (napewno mniej lub tyle samo dominuje)

następnie, sprawdzam ile dla każdego x (max y), odejmuje wszystkie punkty, które są:
 - większe na y
 - większe na x
(pozornie jest problem, że odejme punkty >x i >y podwójnie, jednakże
punkt który dominuje najwięcej, nie posiada nic >x >y, (byłby wtedy dominowany))
'''

def dominance(P):
  # tu prosze wpisac wlasna implementacje
  n = len(P)
  ilex = [[0,0] for _ in range(n+1)] # ile x, max wys
  iley = [0 for _ in range(n+1)]
  
  for elem in P:
    # print(elem, n)
    ilex[elem[0]] = [1+ilex[elem[0]][0],max(ilex[elem[0]][1],elem[1])]
    # max po y, przy zliaczniu x, bo ten punkt napewno najwiecej dominuje
    iley[elem[1]] +=1

  # sumy prefix-owe
  for i in range(n-1,-1,-1):
    ilex[i][0] = ilex[i+1][0] + ilex[i][0]
    iley[i] = iley[i+1] + iley[i]

  max_dom = 0
  for x in range(n,0,-1):
    wx = ilex[x][0]     # >= na x
    wy = iley[ilex[x][1]] # >= na y
    max_dom = max(max_dom,n - wx - wy + 1)  # +1 bo odejmuje podwójnie rozpatrywany pkt
    # print(x,ilex[x][1],wx,wy,max_dom)

  # print(ilex,"\n",iley)
  return max_dom

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )

# p = [(1, 3), (3, 4), (4, 2), (2, 2), (3,3)]
# dominance(p)


# def dominance(P): # n^2
#   # tu prosze wpisac wlasna implementacje
#   n = len(P)
#   strength = [0 for _ in range(n)] 
#   for i in range(n):
#     for j in range(n):
#       if(P[i][0]>P[j][0] and P[i][1]>P[j][1]):
#         strength[i]+=1
#   return max(strength)