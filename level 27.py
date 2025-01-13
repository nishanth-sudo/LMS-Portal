Develop a program that accepts a string as input and removes characters from the string which appear more than once
input
ITVAC
Gettit
Result
ITVAC
Gei
Code:
  s=input()
  re=[]
  c={}
  for i in s:
      c[i]=c.get(i,0)+1
  for j in s:
      if c[j]==1:
          re.append(j)
  print("".join(re))
