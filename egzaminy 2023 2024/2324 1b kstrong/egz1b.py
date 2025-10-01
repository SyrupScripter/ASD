from egz1btesty import runtests

'''
złożoność wzorcowa - O(nk)

tworze tablice sumy dp o rozmiarze n*k, następnie rozpatruje kazdy element
jezeli go nie biore to biore sume poprzednich i zwiększam indeks w strone k
'''

def kstrong(T, k):
  # tu prosze wpisac wlasna implementacje
  n = len(T)

  dp = [[0 for _ in range(k+1)] for _ in range(n)]
  dp[0][0] = T[0]

  for i in range(1,n):    # max suma
    dp[i][0] = max(dp[i-1][0] + T[i],T[i])

  maks=0
  for j in range(1,k+1):
    # dp[0][j] = 0
    for i in range(1,n):
      dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]+T[i],dp[i][j])
      maks = max(dp[i][j],maks)
  
  return maks


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )
