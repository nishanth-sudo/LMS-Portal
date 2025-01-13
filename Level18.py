Write a program to display the pattern given below.
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
Code:
  n=int(input())
  for i in range(1,n+1):
      print((str(i)+' ')*i)

*
* *
* * *
Code:
  n=int(input())
  for i in range(1,n+1):
      print("* "*i)

1
1 1
Code:
  n=int(input())
  for i in range(1,n+1):
      print('1 '*i)(str
input
3
result
*
# #
* * *
Code:
  n=int(input())
  if n<0:
      print("Invalid input")
  else:
      for i in range(1,n+1):
          if i%2!=0:
              print("* "*i)
          else:
              print("# "*i)
