Write a program to print the following pattern:
11
12 13
14 15 16
Code:
  c=11
  for i in range(1,int(input())+1):
      for j in range(i):
          print(c,end=' ')
          c+=1
      print()

1
1 2 
1 2 3
Code:
for i in range(1,int(input())+1):
    print(" ".join(str(j) for j in range(1,i+1)))

1
2 2
3 3 3
Code:
  for i in range(1,int(input())+1):
      print((str(i)+' ')*i)

A
A B
A B C
Code:
n=int(input())
c=ord('A')
for i in range(1,n+1):
    print(' '.join(chr(c+j) for j in range(i)))
