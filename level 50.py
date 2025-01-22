sparse matrix program
input
3 3
1 0 3
0 0 4
6 0 0
result
Sparse matrix
Code:
r,c=map(int,input().split())
m=[]
for i in range(r):
    e=list(map(int,input().split()))
    m.append(e)
zc=sum(r.count(0) for r in m)
t=r*c
if zc< t/2:
    print("The given matrix is not a Sparse matrix")
else:
    print("The given matrix is Sparse matrix")
