n,m = map(int,input().split())
d = {'XS':0,'S':0,'M':0,'L':0,'XL':0,'XXL':0}
s = []
arr = []
f = 0
for i in range(m):
    a,b = input().split()
  #  print(a)
 #   print(b)
    d[a]+=1
    d[b.strip()]+=1
    arr.append((a,b.strip()))
for i in d.keys():
    if d[i] > n:
        s.append(i)
#print(s)
for i in range(len(s)):
    for j in range(len(s)):
        if i!=j:
            if arr.count((s[i],s[j]))+arr.count((s[j],s[i])) > 1:
                f = 1
if f== 0:
    print('YES')
else:
    print('NO')