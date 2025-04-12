#heapify - kopcujemy / sprawdzamy czy poprawny kopiec
#buildheap - robimy heapify na całości

from math import floor

def heapify(A, n, i): #A - array, n - ilość elementów, i - index
    l = 2*i+1 #lewy pan
    r = 2*i+2 #prawy pan
    max_ind = i
    
    if(l<n and A[l]>A[max_ind]):
        max_ind = l
    if(r<n and A[r]>A[max_ind]):
        max_ind = r
    if max_ind != i:        #jezeli zobaczymy, że wartość dla lewego lub prawego > parent, to zamiana
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def build_heap(A):
    n = len(A)
    for i in range(floor((n-1)/2)-1,-1,-1):
        heapify(A,n,i)

def heapsort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1,0,-1): #znajdujemy max element dajemy na czubek i popujemy, n-1 bo ostatni posort. zostanie
        A[i], A[0] = A[0], A[i]
        heapify(A,i,0)
        print(T)
    return T


T = [1,2,3,4,5,6,7,3]

print(heapsort(T))