from egz2atesty import runtests

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    n = len(A)
    
    filled = [0 for _ in range(n)]
    
    last = -1
    for i in range(n):
        for j in range(n):
            if(filled[j]+A[i])<=T:
                filled[j]+=A[i]
                last = j
                break

    return last

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
