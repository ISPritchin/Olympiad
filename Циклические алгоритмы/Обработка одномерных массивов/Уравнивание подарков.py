# https://codeforces.com/problemset/problem/1399/B


def read_arr():
    return [int(x) for x in input().split()]


N_SETS = int(input())

for i in range(N_SETS):
    n_pairs = int(input())
    bs = read_arr()
    cs = read_arr()
    m = min(min(bs), min(cs))
    min_bs = min(bs)
    min_cs = min(cs)
    bs = [x - min_bs for x in bs]
    cs = [x - min_cs for x in cs]
    res = 0
    for b, c in zip(bs, cs):
        res += max(b, c)
    print(res)
