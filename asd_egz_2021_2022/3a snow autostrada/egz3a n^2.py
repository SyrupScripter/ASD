from egz3atesty import runtests

def snow( T, I ):
    # tu prosze wpisac wlasna implementacje
    droga = [0 for _ in range(T)]

    for pocz,kon in I:
        for i in range(pocz,kon+1):
            droga[i]+=1

    return max(droga)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
