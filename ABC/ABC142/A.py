# coding: utf-8

n = int(input())
ans = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        ans += 1


print(ans/n)
