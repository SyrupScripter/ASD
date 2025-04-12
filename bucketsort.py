from random import randint

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j=i-1
        #print(arr[j], arr[j+1])
        while(j>=0 and arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1], arr[j]
            j-=1
        
    return arr

#normalizacja danych do bucketsorta
def normalizedata(T):   #np. 20-100
    n = len(T)
    
    mx = max(T) #100
    mi = min(T) #20
    delta = mx - mi + 1 #80, +1 bo inaczej max elem wyjdzie poza tab

    # 20->0
    for i in range(n):
        T[i]=T[i]-mi
        T[i]=T[i]/delta

    return T,delta,mi


def bucketsort(T): # osobna normalizacja
    T,delta,mi = normalizedata(T)
    n = len(T)

    buckets = [[] for _ in range(n)]

    for i in range(n):
        #print(int(T[i]*n), n, "pies", T[i])
        buckets[int(T[i]*n)].append(T[i])

    for i in range(n):
        if(len(buckets[i])>1):
            buckets[i] = insertion_sort(buckets[i])

    k=0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[k]=buckets[i][j]
            k+=1

    for i in range(n):
        T[i]=round(T[i]*delta+mi)

def bucketsortv2(T): #bucketsort + normalizacja danych
    n = len(T)

    buckets = [[] for _ in range(n)]

    #normalizacja
    mx = max(T) #100
    mi = min(T) #20
    delta = mx - mi + 1 #80, +1 bo inaczej max elem wyjdzie poza tab

    for i in range(n):
        buckets[int(((T[i]-mi)/delta)*n)].append(T[i])
        #print(int(((T[i]-mi)/delta)*n))

    #print(buckets)

    #sortowanie osobno kubełków
    for i in range(n):
        if(len(buckets[i])>1):
            buckets[i] = insertion_sort(buckets[i])

    #połączenie
    k=0
    for i in range(n):
        for j in range(len(buckets[i])):
            T[k]=buckets[i][j]
            k+=1


for _ in range(10):
    a = [randint(5,200) for _ in range(50)]
    expected = sorted(a)

    bucketsortv2(a)

    #print(a, expected)
    assert a == expected
    print(a, "ok")