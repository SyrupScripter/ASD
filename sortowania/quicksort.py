#lomuto scheme
def partition(T, s, f):     #binary search
    i = s
    #T[(s+f)//2],T[f] = T[f],T[(s+f)//2]        # replace middle element for comparision, in case list is sorted
    for j in range(s,f):
        if(T[j] <= T[f]):
            T[i],T[j]=T[j],T[i]
            i+=1

    T[i],T[f] = T[f], T[i]
    return i 

T = [1, 9, 8, 4, 7, 2, 15]

#partition(T, 0, len(T))

def quicksort(T, s, f):
    if s < f:
        q = partition(T, s, f)
        #print(T, s, f, q)
        quicksort(T, s, q-1)
        quicksort(T, q+1, f)

quicksort(T, 0, len(T)-1)
print(T)