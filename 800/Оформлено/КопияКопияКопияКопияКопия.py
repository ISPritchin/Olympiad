n = int(input())
for i in range(n):
    _ = input()
    a = [int(x) for x in input().split()]
    print(len(set(a)))
