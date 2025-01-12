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
