fibonacci series
input
5
result
0 1 1 2 3
Code:
  n=int(input())
  a,b=0,1
  co=0
  while co<n:
      print(a,end=' ')
      c=a+b
      a=b
      b=c
      co+=1
