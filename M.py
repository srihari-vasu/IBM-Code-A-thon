from itertools import combinations

x,r = map(int,input().split())
arr = list(map(int,input().split()))
m = x-r
a=list(combinations(arr, m))
d=[]

for i in a:
    b = -99999999999999
    c = 999999999999999
    j = sorted(i)
    for k in range(len(j)):
        for l in range(len(j)):
            if k!=l:
                if b < abs(j[k]-j[l]):
                    b = abs(j[k]-j[l])
                if c > abs(j[k]-j[l]):
                    c = abs(j[k]-j[l])
    d.append(b+c)
print(min(d))