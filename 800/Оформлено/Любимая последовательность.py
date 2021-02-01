n_sets = int(input())
for i in range(n_sets):
    _ = int(input())
    seq = list(map(int, input().split()))
    left = 0
    right = len(seq) - 1
    while left <= right:
        if left == right:
            print(seq[left], end=" ")
        else:
            print(seq[left], end=" ")
            print(seq[right], end=" ")
        left += 1
        right -= 1
    print()
