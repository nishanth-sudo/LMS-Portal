python program to hop one letter and print the string as given
input
string 
printlno
Result
srn
pitn
Code:
  s=input()
  re=''
  for i in range(0,len(s),2):
      re+=s[i]
  print(re)

Search for a substring within a string
For example:
Input	Result
Hello World
World
Starts at position 6
Friends are always there
always
Starts at position 13
HelloWorld
world
-1
Code:
  st=input()
  k=input()
  p=st.find(k)
  if k in st:
      print("Starts at position",p+1)
  else:
      print(p)

programto find the two strings are equal
input
howareyou howareyou
result
strings are equal
Code:
  s,t=map(str,input().split())
  if s==t:
      print("Strings are equal")
  else:
      print("Strings are not equal")
