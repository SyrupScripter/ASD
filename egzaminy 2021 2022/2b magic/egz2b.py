from egz2btesty import runtests

'''
max_sztabki[n] - maksymalna liczba sztuka sztabek w komnacie n

'''
def magic( C ):
    # tu prosze wpisac wlasna implementacje
    n = len(C)

    msztabki = [-1 for _ in range(n)]
    msztabki[0] = 0

    for i in range(n):
        if(msztabki[i]==-1):    # nie da sie wejsc
            continue
        ile_zlota = C[i][0]
        portfel = msztabki[i] + ile_zlota   # nasza kieszeń + skrzynia
        for j in range(1,4):
            koszt, dokad = C[i][j][0], C[i][j][1]
            # czy: idziemy do przodu, nas stać, mozemy wziąść na tyle złota
            if(dokad > i and portfel - koszt >= 0 and ile_zlota - koszt <= 10):  
                msztabki[dokad] = max(msztabki[dokad], min(portfel - koszt, msztabki[i] + 10))
                # print(msztabki[dokad],i,j)
    # print(*C,"\n",msztabki, sep="\n")
    return msztabki[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
