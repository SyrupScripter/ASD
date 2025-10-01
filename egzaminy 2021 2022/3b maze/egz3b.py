from egz3btesty import runtests

'''
algorytm idzie sweepem od góry, zapisując największą możliwą ilość kroków 
(z poprzedniego pola u góry, lub z lewej)

następnie analogicznie sweep od dołu, przy czym rozpatrujemy, bez kroków od góry w tej samej kolumnie
(przez każde pole możemy przejść max 1 raz)

dla uproszczenia sweep od góry identyczny jak od dołu
'''

def maze( L ):
    # tu prosze wpisac wlasna implementacje
    n = len(L)
    dp = [[float('-inf') for _ in range(n)] for _ in range(n)]
    
    # base case
    for i in range(0,n):
        if(L[i][0]!='#'):
            dp[i][0] = i
        else:
            break
    
    for i in range(1,n):    # idziemy kolumnami, pierwsza kolumna wypełniona
        prev = float('-inf')
        # dp[0][i] = dp[0][i-1] 
        for j in range(n):
            if(L[j][i]!='#'):
                prev = max(prev+1,dp[j][i-1]+1)
                dp[j][i] = max(dp[j][i],prev)
            else:
                prev = float('-inf')
        
        # dp[n-1][i] = max(dp[n-1][i],dp[n-1][i-1])
        prev = float('-inf')
        
        for j in range(n-1,-1,-1):
            if(L[j][i]!='#'):
                prev = max(prev+1,dp[j][i-1]+1)
                dp[j][i] = max(dp[j][i],prev)
            else:
                prev = float('-inf')

    return dp[n-1][n-1] if dp[n-1][n-1] != float('-inf') else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
