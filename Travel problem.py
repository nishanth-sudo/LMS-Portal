s,x,n=map(int,input().split())
exc=[tuple(map(int,input().split()))for _ in range(n)]
ex_days={t:y for t,y in exc}
c_day=1
tot=0
while tot<s:
    if c_day in ex_days:
        tot+=ex_days[c_day]
    else:
        tot+=x
    c_day+=1
res=c_day-1
print(res)
