print square of the elements in the array. array is in unsorted form
input
5
-9 -2 0 2 3
result
0 4 4 9 81]
Code:
  n=int(input())
  ar=list(map(int,input().split()))
  re=[]
  for i in ar:
      r=i**2
      re.append(r)
  re.sort()
  print(*re)

remove duplicates
input
1,1,2
result
1,2
Code:
  ar=[int(x) for x in input().split(',')]
  re=set(ar)
  s=sorted(re)
  print(",".join(map(str,s)))

find second lowest number in the array
input 
5
10
20
30
40
50
result
20
Code:
  n=int(input())
  ar=[]
  for i in range(1,n+1):
      e=int(input())
      ar.append(e)
  ar.sort()
  print(ar[1])
