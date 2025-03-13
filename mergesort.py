#ponizej odbedzie sie pierwsza (prawdopodobnie katastroficzna) próba napisania merge sort

def merge(a:list, b:list):

    c = []

    p=q=0
    while(a and b and p<len(a) and q<len(b)):
        #print(a[p], b[q], p, q)
        if(a[p] <= b[q]):
            c.append(a[p])
            p+=1
            
        else:
            c.append(b[q])
            q+=1
    #print(p, len(a), q, len(b), a, b)
    
    while(a and p<len(a)):
        c.append(a[p])
        p+=1
    while(b and q<len(b)):
        c.append(b[q])
        q+=1
    
    return c

def mergesort(a):
    if(len(a)==1):
        return a
    
    b=[]
    c=[]
    #print(a, b, c)

    for i in range(len(a)//2):
        b.append(a[i]) 
    for i in range(len(a)//2, len(a)):
        c.append(a[i])
    print(a, b, c)

    b = mergesort(b)
    c = mergesort(c)

    return merge(b,c)
    
print(mergesort([1,6,1,4,5,8,9,10,3]))