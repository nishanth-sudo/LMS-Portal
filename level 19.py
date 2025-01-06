Write a program to print the following pattern:
A
B C
D E F
Code:
  n=int(input())
  ch=ord('A')
  for i in range(1,n+1):
      for j in range(i):
          print(chr(ch),end=' ')
          ch+=1
      print()

1
2 3 
4 5 6
Code:
  c=1
  for i in range(1,int(input())+1):
      for j in range(i):
          print(c,end=' ')
          c+=1
      print()
    

    A
  C C C
E E E E E
Code:
  n=int(input())
  a=ord('A')
  for i in range(1,n+1):
      l=chr(a)
      s=(n-i)*2
      print(' '*s,end='')
      print((l+' ')*(2*i-1))
      a+=2
