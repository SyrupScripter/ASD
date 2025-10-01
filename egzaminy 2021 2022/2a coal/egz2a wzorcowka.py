from egz2atesty import runtests
from math import log2
from math import ceil
'''
O(nlogn) - użycie segment tree

idea: przy szukaniu magazynu, można użyć struktury segment tree, gdzie liście to
magazyny, następnie, aby nie przeszukiwać wszystkich magazynów pokolei w parentach magazynów
możemy trzymać informacje o magazynach niżej (max ile możemy jeszcze zmieścić)

dzięki temu insertowanie każdego elementu zajmie tylko O(log(n)) - schodzenie po drzewie
zamiast O(n), więc końcowe time complexity - O(nlog(n))
'''

def insert(cur, load, tree, first_elem):    # obecny element, ile mamy do wsadzenia, drzewo z magazyanmi, pierwszy element
    if(cur >= first_elem):  # doszliśmy do magazynów
        tree[cur]-=load
        return cur

    
    left = cur*2+1
    right = left+1  #cur*2+2

    # print(left,cur)
    if(tree[left]>=load):   # jest miejsce po lewej
        i = insert(left,load,tree,first_elem)
    else:   # miejsce po prawej
        i = insert(right,load,tree,first_elem)

    # aktualizujemy stan magazynów wyżej 
    tree[cur] = max(tree[left],tree[right])

    return i    # zwracamy indeks, gdzie ostatnio wstawilismy węgiel

def coal( A, T ):
    # tu prosze wpisac wlasna implementacje
    n = len(A)
    p = ceil(log2(n))   # najbliższa większa potęga dwójki, na ilosc magazynów
    tree = [T for _ in range(2**(p+1)-1)]   # np. 7 ładunków, 8 mag, 7 dojsc, 7+8 = 2**p-1
    first_element = 2**p-1

    last_idx = None
    for load in A:
        last_idx = insert(0,load,tree,first_element)

    return last_idx - first_element



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )