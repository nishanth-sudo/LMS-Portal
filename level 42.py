Read 2 strings and replace the first occurance of the second string in first string with the third string

If the second string is not there in the first string, then the first string should be displayed as is

For example:

Input	Result
Hello - Are you there?
Are
While
Hello - While you there?
This is a long sentence. is it not?
is
was
This was a long sentence. is it not?

Code:
  import re
  s1 = input()
  s2 = input()
  s3 = input()
  
  s1 = re.sub(r'\b' + re.escape(s2) + r'\b', s3, s1, 1)
  print(s1)

remove nt occurence of a str.
code:
  s=input().split()
  n=int(input())
  w=input()
  l=[]
  c=0
  for i in s:
      if i==w:
          c=c+1
          if c!=n:
              l.append(i)
      else:
          l.append(i)
  print(*l)
