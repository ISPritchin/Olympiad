n_sets = int(input())
for _ in range(n_sets):
    n_st, max_mark = map(int, input().split())
    arr = list(map(int, input().split()))
    r = min(max_mark, sum(arr))
    print(r)
