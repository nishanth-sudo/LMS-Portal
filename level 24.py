print array elements in reverse order:
input   result
5        3
9        4
3        5
5        3
4        9
9
Code:
  n=int(input())
  ar=[]
  for i in range(n):
      ar.append(int(input()))
  ra=ar[::-1]
  for i in ra:
      print(i)

Display the element in the nth index of the array/list
NOTE: Index starts from 0
Input
N - Gives the number of elements in the array/list
N elements of the array
K index of the element to be printed where K is between 0 to N-1
Example
3
10 20 30
0
Output:
10
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  k=int(input())
  print(ar[k])

Write a program to define a function to check whether a particular element is present in the array
Input Format:
Accept array size and its elements and the search key as an input
output Format:
if element is found print: Element is found at index: index
else print: Element not found in array
For example:
Input	Result
5
1 2 3 4 5
3
Element is found at index: 2
5
1 2 3 4 5 
6
Element not found in array
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  k=int(input())
  if k in ar:
      print("Element is found at index:",ar.index(k))
  else:
      print("Element not found in array")

Odd elements of the array:
Code:
  n=int(input())
  ar=[]
  for i in range(1,n+1):
      ar.append(int(input()))
  odd=[x for x in ar if x%2!=0]
  if odd:
      print("Odd items of the array:",*odd)
  else:
      print("No Odd Elements")
