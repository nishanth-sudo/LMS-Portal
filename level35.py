binary pattern
input
2
result
10
01
Code:
  n=int(input())
  for i in range(n):
      r=''
      for j in range(n):
          if (i+j)%2==0:
              r+='1'
          else:
              r+='0'
      print(r)
input
2
result
1     *
2 3 * *
Code:
  n=int(input())
  c=1
  for  i in range(1,n+1):
      for j in range(i):
          print(c,end=' ')
          c+=1 
      print("  "*(n-i)*2,end='')
      print('* '*i)
