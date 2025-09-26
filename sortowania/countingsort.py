def counting_sort(A):
    n = len(A)
    k = max(A)

    count = [0] * (k+1)
    res = [0] * n

    for elem in A:
        count[elem]+=1
    
    for i in range(1,k+1):
        count[i] += count[i-1]
    
    for i in range(n-1,-1,-1):
        res[count[A[i]]-1] = A[i]
        count[A[i]] -= 1
    
    return res


T = [1,4,5,6,1,1,1,4,7]
T = counting_sort(T)
print(*T, sep=' ')