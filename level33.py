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

