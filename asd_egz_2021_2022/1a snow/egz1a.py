from egz1atesty import runtests

def snow( S ):
    # tu prosze wpisac wlasna implementacje
    S = sorted(S, reverse=True)
    n = len(S)

    i=sum=0
    while(i<n):
        if(S[i]-i>0):
            sum += S[i]-i
        else:
            break
        i+=1

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
