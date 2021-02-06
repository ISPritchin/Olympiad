n = int(input())
m = int(input())
if n > len(bin(m)) - 2:
    print(m)
else:
    print(m % 2**n)
