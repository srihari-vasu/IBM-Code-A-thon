n = int(input())
a = list(map(int,input().split()))
b = [-1] * n
b[0] = 0
a = [-1] + a
print(a)
print(b)
for i in range(1,len(a)):
    if b[a[i]-1] == -1:
        temp = 0
        j = a[i]-1
        while(b[j]!=-1):
            temp+=1
            j = a[j]
        b[a[i]-1] = b[j] + temp
    else:
        b[i] = b[a[i]-1]+1
print(b)