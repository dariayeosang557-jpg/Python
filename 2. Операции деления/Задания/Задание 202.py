n = int(input())
m = n * 45 + 5 * (n//2) + 15 * ((n-1)//2)
e = 9 * 60 + m
print(e//60, e%60)

