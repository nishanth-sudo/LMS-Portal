pattern program
input 
3
result
    A
  C C C
E E E E E
Code:
    n=int(input())
    c=ord('A')
    for i in range(n):
      cc=chr(c*2+i)
      print(" "*(n-i-1)*2,end='')
      print(" ".join([cc]*(2*i+1)))

input
5
result
        1  
      2 2  
    3 3 3  
  4 4 4 4  
5 5 5 5 5
Code:
    n=int(input())
    for i in range(1,n+1):
        print(" "*(n-i)*2,end='')
        print((str(i)+' ')*i)

input
3
result
*
# #
* * *
# # #
* * 
#
Code:
    n=int(input())
    for i in range(1,n+1):
        if i%2!=0:
            print('* '*i)
        else:
            print('# '*i)
    for j in range(n,0,-1):
        if j%2!=0:
            print('# '*j)
        else:
            print('* '*j)

input
3
result
    *
  * *
* * *
Code:
    n=int(input())
    for i in range(1,n+1):
        print(" "*(n-i)*2,end='')
        print('* '*i)

input
3
a
result:
  a
 aaa
aaaaa
 aaa
  a
Code:
n=int(input())
s=input()
for i in range(n):
    print(" "*(n-i-1),s*(2*i+1))
for j in range(n-2,-1,-1):
    print(' '*(n-j-1),s*(2*j+1))
