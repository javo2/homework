from math import sqrt
def div(a):
  l=[]
  m=[]
  for i in range(1,int(sqrt(a))+1):
    if a%i==0:
      if a/i==i:
        l.append(i)
      else:
        l.append(i)
        m.insert(0,a/i)
  return(l+m) 

#complexity : O(sqrt(n))
