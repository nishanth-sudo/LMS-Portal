print all numbers from N to 0
input 7 6
result:
7  3  1
6  4  2  0

Ans:
  n=int(input())
  re=[]
  while n>=0:
    if n!=5:
       re.append(n)
    n-=2
   print(*re)


