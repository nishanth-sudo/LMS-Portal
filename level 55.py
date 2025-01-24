 Find the Minimum difference pair
Given an unsorted array, find the minimum difference between any pair in given array.
Sample input 1 5 2 4 5 7 9
Sample output 1
Sample input 1 5 0 0 1 2 3
Sample output Invalid value in array!!!
Input Format
he first line of input contains an integer T denoting the number of test cases. The first line of each test case is N, the size of array. Second line of the test case is the Array
Constraints
1 <= T <= 30 1 < N <= 100 1 <= arr[i] <= 100000
Output Format
Print the minimum difference between any two pairs.
Sample Input 0
1
5
2 4 5 7 9
Sample Output 0
1
Code:
T = int(input())
for _ in range(T):
    n = int(input())
    ar = list(map(int,input().split()))
  
    ar.sort()
    d=float('inf')
    for i in range(1,n):
        d=min(d,ar[i]-ar[i-1])
print(d)

print Array in zig zag order
input
5
31
32
33
34
35
result
[31,33,32,35,34]
Code:
n = int(input())
ar=[]
for i in range(1,n+1):
    e=int(input())
    ar.append(e)
for i in range(1,n-1,2):
    ar[i],ar[i+1]=ar[i+1],ar[i]
print(ar)
