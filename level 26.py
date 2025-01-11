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
