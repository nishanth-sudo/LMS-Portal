Write a program to read the 3x5 matrix. Add the elements in each column and display it.
Example:
Input:
12 14 15 23 56
12 78 34 12 12
23 14 13 15 26
Output:
47 106 62 50 94
Code:
  m=[]
  for i in range(3):
      r=list(map(int,input().split()))
      m.append(r)
  print(*[sum(c) for c in zip(*m)])

program to print add and subtraction of two 2d matrices
input
2 2
2 2

1 2 
3 4

4 5 
6 7

Code:
  r1,c1=map(int,input().split())
  r2,c2=map(int,input().split())
  if r1<0 and c1<0:
      print("Row and column size should not be negative")
  elif r1!=c1:
      print("Row and column size should be same for 2 matrices")
  else:
      m1=[]
      for i in range(r1):
          e1=list(map(int,input().split()))
          m1.append(e1)
      m2=[]
      for i in range(r2):
          e2=list(map(int,input().split()))
          m2.append(e2)
      add=[[m1[i][j]+m2[i][j] for j in range(c1)] for i in range(r1)]
      sub=[[m1[i][j]-m2[i][j] for j in range(c1)] for i in range(r1)]
      print("Addition:")
      for i in add:
          print(*i)
      print("Subtraction:")
      for j in sub:
          print(*j)

find primary and secondary diagonal elements:\
input
2
2
1
2
3
4

Result
Primary diagonal elements:
1
4
Secondary diagonal elements:
2
3
Code:
  r=int(input())
  c=int(input())
  if r!=c:
      print("Row and column size should be same")
  elif r<0 and c<0:
      print("Row and column size should not be negative")
  else:
      m=[]
      for i in range(r):
          e=[]
          for j in range(c):
              e.append(int(input()))
          m.append(e)
      print("Primary diagonal elements:")
      for i in range(r):
          print(m[i][i])
      print("Secondary diagonal elements:")
      for i in range(r):
          print(m[i][r-i-1])

Program to find sum of right diagonal elements in matrix
input:
2
15 48
10 37
Result
52
Code:
  r=int(input())
  m=[]
  for i in range(r):
      e=list(map(int,input().split()))
      m.append(e)
  s=0
  for i in range(r):
      for j in range(r):
          if i==j:
              s=s+m[i][j]
  print("Addition of the right Diagonal elements is:",s)


transpose of the given matrix
input
2
3
11
22
34
41
53
65
Result
11 41
22 53
34 65
Code:
  import numpy as np
  r=int(input())
  c=int(input())
  e=[int(input()) for _ in range(r*c)]
  m=np.array(e).reshape(r,c)
  t=m.T
  for k in t:
      print(*k)

square of each element in a matrix
2 2

1 2
3 4
Result
1 4
9 16
Code:
  import numpy as np
  r,c=map(int,input().split())
  m=np.array([list(map(int,input().split())) for _ in range(r)])
  re=np.square(m)
  for i in re:
      print(*i)

print difference between two matrices
2 2
5 5
5 5
2 2
4 3
2 1
Result
1 2
3 4
Code:
  import numpy as np
  r1,c1=map(int,input().split())
  m1=np.array([list(map(int,input().split())) for _ in range(r1)])
  
  r2,c2=map(int,input().split())
  m2=np.array([list(map(int,input().split())) for _ in range(r2)])
  
  if r1==c1 and r2==c2:
      re=m1-m2
      for i in re:
          print(*i)
  else:
      print("Matrix Subtraction Not Possible")

sum of first column in a 2d matrix
input
5
6
7
8
result
12
Code:
  import numpy as np
  e=[int(input()) for _ in range(2*2)]
  m=np.array(e).reshape(2,2)
  re=np.sum(m[:,0])
  print(re)
