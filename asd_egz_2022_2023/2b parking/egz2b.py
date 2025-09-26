from egz2btesty import runtests

'''
F(i,j) = min(F(i-1,x)+f(i,x))

(i, j) = minimalna suma odległości biurowców z pozycji 
X[0], . . . , X[i] do przydzielonych im
działek, przy założeniu że biurowiec z pozycji X[i] ma 
przydzieloną działkę z pozycji Y[j].
'''

def parking(X,Y):
  # tu prosze wpisac wlasna implementacje
  n = len(X)
  m = len(Y)
  
  dp = [[float('inf') for _ in range(m)] for _ in range(n)]
  # dp - suma najlepszych wyborow

  dp[0][0] = abs(X[0] - Y[0])

  for x in range(1, m): # base case
    dp[0][x] = min(abs(X[0] - Y[x]),dp[0][x-1])

  for i in range(1,n):  # biurowce, poza pierwszym
    for j in range(i, m):  # parkingi, poza zajetymi
      dp[i][j] = min(dp[i-1][j-1]+abs(X[i] - Y[j]), dp[i][j-1])
  return min(dp[n-1])
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
