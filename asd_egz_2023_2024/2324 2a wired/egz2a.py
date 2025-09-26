from egz2atesty import runtests

def wired( T ):
    n = len(T)
    min_cost = [[float('inf') for _ in range(n)] for _ in range(n)]
    # minimalny koszt z t[i] - t[j]

    def cost(i,j):
        nonlocal T
        return abs(T[i]-T[j])+1

    def solve(i,j):
        nonlocal min_cost,n
        if(j==i+1):   # jak sa obok siebie
            return cost(i,j)
        # print(n,i,j)
        if(min_cost[i][j]!=float('inf')):
            return min_cost[i][j]
        
        l = j-i # 3-0, 4-1
        mini = solve(i+1,j-1) + cost(i,j)   # zawężamy o jeden z każdej strony
        for mv in range(2,l,2):
            # print('pies')
            mini = min(mini, solve(i,i+mv-1) + solve(i+mv,j ))
    
        # print(i,j,n)
        min_cost[i][j] = mini
        return mini
    
    # print(*min_cost,sep="\n")
    return solve(0,n-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )

