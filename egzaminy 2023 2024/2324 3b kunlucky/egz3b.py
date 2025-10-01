from egz3btesty import runtests

def make_unlucky(k,m):
  xi=k
  i=1
  
  my_set = set()

  while(xi<=m): # na wszelki wypadek <=
    my_set.add(xi)
    xi = xi + xi % i + 7
    i+=1

  return my_set


def kunlucky(T, k):
  # tu prosze wpisac wlasna implementacje

  # if(len(T)>30):
  #   return 0

  max_T = max(T)

  unlucky_nums = make_unlucky(k,max_T)  # set unlucky liczb
  # print(unlucky_nums)

  maxdl = 0
  n = len(T)

  ile_unlucky=0

  l=m=p=0
  for i in range(n):
    if(T[i] in unlucky_nums):
      # sprawdzamy czy dluzsze
      ile_unlucky+=1
      if(ile_unlucky == 1):
        p = i
      elif(ile_unlucky == 2):
        m = p
        p = i
      else:
        l = m
        m = p
        p = i
    else:
      if(i-l>maxdl):
        maxdl = i-l
        # print(i,p,m,l)


  return maxdl


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kunlucky, all_tests = True )
