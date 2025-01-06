To print the following Pattern:
1 1 1
2 2 2
3 3 3
Code:
n=int(input())
for i in range(1,n+1):
    print(f"{i} "*n)

* * 
* *
Code:
 n=int(input())
 for i in range(1,n+1):
     print('*'*n)

1 2 
1 2
Code:
 n=int(input())
 for i in range(n):
     print(" ".join(str(i) for i in range(1,n+1)))

A B
A B
Code:
 print(" ".join(chr(ch+i) for i in range(n)))
