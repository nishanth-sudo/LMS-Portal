password decoding
n=int(input())
ar=list(map(int,input().split()))
s=[]
for i in ar:
    while i>=10:
        i=sum(int(d) for d in str(i))
    s.append(i)
oa={1:'a',3:'c',5:'e',7:'g',9:'i'}
p=''
for k in s:
    p+=oa.get(k,str(k))
print(p)
