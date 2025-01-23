two sum solution
input
2 6 11 3
9
result
index1:1
index2:3
Code:
ar=[int(x) for x in input().split()]
t=int(input())
f=False
for i in range(1,len(ar)):
    for j in range(i):
        if ar[i]+ar[j]==t:
            print("Index1:",j,"\nIndex2:",i)
            f=True
            break
        if f:
            break
if not f:
    print("No two sum solution")

Removes k digits from num to obtain the smallest possible number.
input
10200
1
Code:
n=input()
k=int(input())
r=[]
for d in n:
    while r and r[-1]>d and k:
        r.pop()
        k-=1
    r.append(d)
if k>0:
    r=r[:-k]
re="".join(r).lstrip("0")
print(re)

You are given a nested list of integers nestedList. 
Each element is either an integer or a list whose elements may also be integers or other lists. The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth. 
Return the sum of each integer in nestedList multiplied by its depth. Input: nestedList = [[1,1],2,[1,1]] Output: 10 Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Code:
ar=eval(input())
t=0
s=[(ar,1)]
while s:
    cl,cd=s.pop()
    for i in cl:
        if isinstance(i,list):
            s.append((i,cd+1))
        else:
            t+=i*cd
print(t)            
