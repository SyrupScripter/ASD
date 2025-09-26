def bsearch(arr, x):
    l = 0
    r = len(arr)-1
    m = (l+r)//2
    while(l<=r):
        m = (l+r)//2
        if(arr[m]>x):
            r = m-1
        elif(arr[m]<x):
            l = m+1
        else:
            return m
    
    print('not found',m)
    return m
