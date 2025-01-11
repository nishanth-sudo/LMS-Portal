add two array:
5 
10 20 30 40 50
1 2 3 4 5
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  a1=list(map(int,input().split()))
  for i in range(n):
      print(ar[i]+a1[i],end=' ')

add only +ve elements in array:
5
10 -20 30 -40 50
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  tot=0
  for i in ar:
      if i>0:
         tot+=i
  print(tot)

sum of 'n' elements in array:
5 
10 20 3 40 50
3
33
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  t=int(input())
  print(sum(ar[:t]))

Add the first and last element in the array and report if the sum is odd or even
For example:
Input	
5
10 20 30 40 50
Result
60
EVEN
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  re=ar[0]+ar[n-1]
  print(re)
  if re%2==0:
      print("EVEN")
  else:
      print("ODD")
