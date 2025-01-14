pattern
input
3
result
F
E D
C B A
Code:
  n=int(input())
  s=ord('A')+(n*(n+1))/2-1
  for i in range(1,n+1):
      r=[]
      for k in range(i):
          r.append(chr(s))
          s-=1
      print(*r)

input
3
Result
6 5 4
3 2
1
Code:
  n=int(input())
  s=(n*(n+1))//2
  for i in range(n,0,-1):
      r=[]
      for j in range(i):
          r.append(chr(s))
          s-=1
      print(*r)
input
4
result
      J
    I H
  G F E
D C B A
Code:
  n=int(input())
  s=ord('A')+(n*(n+1))//2-1
  for i in range(1,n+1):
      r=[]
      for k in range(i):
          r.append(chr(s))
          s-=1
      print(" "*(2*(n-i))+" ".join(r))

