n = int(input())
a = list(map(int, input().split()))
b = [a[0]]
for i in a[1:-1]:
    if i > 0:
        b.append(i)
if n>1:
    b.append(a[-1])
print(sum(b))