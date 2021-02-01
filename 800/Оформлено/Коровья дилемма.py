n_sets = int(input())

for i in range(n_sets):
    n = int(input())
    arr = list(map(int, input().split()))
    lens = set()
    for i in range(n):
        for j in range(i+1, n):
            l = arr[j] - arr[i]
            if l not in lens:
                lens.add(l)
    print(len(lens))
