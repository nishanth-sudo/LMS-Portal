input
3
result
1 2 3
  2
1 2 3
Code:
n=int(input())
for i in range(1,n+1):
    print(i,end=' ')
print()
for i in range(1,n-1):
    print(" "*(2*(n-i-1))+str(n-i))
for i in range(1,n+1):
    print(i,end=' ')

input
3
result
1
2*3
4*5*6
4*5*6
2*3
1
Code:
n=int(input())
c=1
for i in range(1,n+1):
    r=[]
    for j in range(i):
        r.append(str(c))
        c+=1
    print("*".join(r))
c-=1
for i in range(n,0,-1):
    s=[]
    for j in range(i):
        s.append(str(c))
        c-=1
    print("*".join(reversed(s)))

input
4
result
   *
  * *
 *   *
*     *
 *   *
  * *
   *
Code:
   *
  * *
 *   *
*     *
 *   *
  * *
   *
