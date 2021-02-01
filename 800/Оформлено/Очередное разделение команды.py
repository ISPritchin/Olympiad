n_sets = int(input())
for i in range(n_sets):
    _ = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    last = arr[0]
    for i in range(1, len(arr)):
        current = arr[i]
        if last + 1 == current:
            print(2)
            break
        last = current
    else:
        print(1)
