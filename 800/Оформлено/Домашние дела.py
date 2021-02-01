n, a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
end_b = arr[b-1]
start_a = arr[b]
if end_b < start_a:
    print(start_a - end_b)
else:
    print(0)
