Kaprekar number program:
  n=int(input())
  b=str(n**2)
  c=int(b[:2])+int(b[2:])
  if c==n and n==c:
      print("Kaprekar Number")
  else:
      print("Not a Kaprekar Number")

Palindrome Program:
s=input()
print("Palindrome" if s[::-1]==s else "Not a palindrome")
321 Palindrome

progrma to read number from user and print it in words:
Code:
  n=int(input())
  w={
      0:'Zero',
      1:'One',
      2:'Two',
      3:'Three',
      4:'Four',
      5:'Five',
      6:'Six',
      7:'Seven',
      8:'Eight',
      9:'Nine'
  }
  re=[]
  while n>0:
      d=n%10
      re.append(w[d])
      n//=10
  print(*re[::-1])

input    result
4372     Four Three Seven Two
