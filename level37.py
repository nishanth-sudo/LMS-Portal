program to find position where number sequence decreases
input
5
10
20
30
5
15
result
5
Code:
  n=int(input())
  ar=[]
  for i in range(n):
      e=int(input())
      ar.append(e)
  re=-1
  for i in range(1,len(ar)):
      if ar[i]<ar[i-1]:
         re=i+1
         break
  print(re)

