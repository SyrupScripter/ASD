from egz1btesty import runtests

'''
dp[n][E] - minimalny dystans aby dostac sie na planete z E paliwem pozostalym
'''

def planets( D, C, T, E ):
    # tu prosze wpisac wlasna implementacje
    n = len(D)
    dp = [[float('inf') for _ in range(n)] for _ in range(E+1)]

    for i in range(E+1):
        dp[i][0] = C[0]*i

    dokad, koszt = T[0]     # rozpatrujemy jeszcze pierwszy teleport
    dp[0][dokad] = koszt

    for i in range(1,n):
        dystans = D[i] - D[i-1]
        for j in range(E+1):  # dolatujemy z poprzedniej planety
            if(j-dystans>=0):
                dp[j-dystans][i] = min(dp[j-dystans][i], dp[j][i-1])
        
        for j in range(1,E+1):
            dp[j][i] = min(dp[j][i], dp[j-1][i]+C[i])

        #teleport
        dokad, koszt = T[i]
        if(dokad == i): continue # nie działający teleport
        dp[0][dokad] = min(dp[0][dokad], dp[0][i]+koszt)
        # print("tp", dokad, dp[0][dokad], C[dokad])
        

    min_koszt = float('inf')
    for i in range(E+1):
        min_koszt = min(min_koszt,dp[i][n-1])
    

    # dp2 = [[float('inf') for _ in range(E+1)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(E+1):
    #         dp2[i][j] = dp[j][i]
    # print(*dp2, sep="\n")

    return min_koszt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
